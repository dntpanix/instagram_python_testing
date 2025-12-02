from abc import ABC, abstractmethod
from typing import Optional
from framework.logger import log_action, log_waning
try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.select import Select
except ImportError:
    log_waning("Selenium not installed, SeleniumElementActions will not work")

class BaseElementActions(ABC):
    """Abstract element actions interface"""

    @abstractmethod
    def click(self, x_offset: int = 0, y_offset: int = 0, hold_seconds: float = 0):
        pass

    @abstractmethod
    def right_click(self, x_offset: int = 0, y_offset: int = 0):
        pass

    @abstractmethod
    def send_keys(self, text: str, clear_first: bool = True):
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def get_attribute(self, attr_name: str) -> Optional[str]:
        pass

    @abstractmethod
    def select_by_text(self, text: str):
        pass


class SeleniumElementActions(BaseElementActions):
    """Selenium element actions implementation"""

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

    @log_action("Clicking element")
    def click(self, x_offset: int = 0, y_offset: int = 0, hold_seconds: float = 0):
        """Click element with offset and hold duration"""
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.element, x_offset, y_offset).pause(
            hold_seconds
        ).click().perform()

    @log_action("Right-clicking element")
    def right_click(self, x_offset: int = 0, y_offset: int = 0):
        """Right-click element"""
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(
            self.element, x_offset, y_offset
        ).context_click().perform()

    @log_action("Sending keys")
    def send_keys(self, text: str, clear_first: bool = True):
        """Type text into element"""
        if clear_first:
            self.element.clear()
        text = text.replace("\n", "\ue007")
        self.element.send_keys(text)

    @log_action("Getting text")
    def get_text(self) -> str:
        """Get element text"""
        return self.element.text or ""

    @log_action("Getting attribute")
    def get_attribute(self, attr_name: str) -> Optional[str]:
        """Get element attribute"""
        return self.element.get_attribute(attr_name)

    @log_action("Selecting by text")
    def select_by_text(self, text: str):
        """Select option from dropdown by visible text"""
        select = Select(self.element)
        select.select_by_visible_text(text)


class PlaywrightElementActions(BaseElementActions):
    """Playwright element actions implementation"""

    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    @log_action("Clicking element")
    def click(self, x_offset: int = 0, y_offset: int = 0, hold_seconds: float = 0):
        """Click element with offset and hold duration"""
        kwargs = {}
        if x_offset or y_offset:
            kwargs["position"] = {"x": x_offset, "y": y_offset}
        if hold_seconds:
            kwargs["delay"] = int(hold_seconds * 1000)

        self.locator.click(**kwargs)

    @log_action("Right-clicking element")
    def right_click(self, x_offset: int = 0, y_offset: int = 0):
        """Right-click element"""
        kwargs = {"button": "right"}
        if x_offset or y_offset:
            kwargs["position"] = {"x": x_offset, "y": y_offset}

        self.locator.click(**kwargs)

    @log_action("Sending keys")
    def send_keys(self, text: str, clear_first: bool = True):
        """Type text into element"""
        if clear_first:
            self.locator.clear()
        self.locator.fill(text)

    @log_action("Getting text")
    def get_text(self) -> str:
        """Get element text"""
        return self.locator.text_content() or ""

    @log_action("Getting attribute")
    def get_attribute(self, attr_name: str) -> Optional[str]:
        """Get element attribute"""
        return self.locator.get_attribute(attr_name)

    @log_action("Selecting by text")
    def select_by_text(self, text: str):
        """Select option from dropdown by visible text"""
        self.locator.select_option(text)
