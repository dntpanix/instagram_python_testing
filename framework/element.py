"""Main element abstraction - supports both Selenium and Playwright"""

from typing import Optional, List, Any
from framework.logger import log_action, setup_logger
from framework.locator import Locator, DriverType


class WebElement:
    """Type-safe WebElement abstraction supporting both Selenium and Playwright"""

    def __init__(
        self,
        locator: Locator,
        driver: Any,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        self._locator = locator
        self._driver = driver
        self._driver_type = driver_type
        self._timeout = timeout
        self._logger = setup_logger(self.__class__.__name__)

        self._initialize_managers()

    def _initialize_managers(self):
        """Initialize appropriate managers based on driver type"""
        if self._driver_type == DriverType.SELENIUM:
            from framework.waiter import SeleniumWaitManager
            from framework.screenshot import SeleniumScreenshotManager

            self._wait_manager = SeleniumWaitManager(self._driver, self._timeout)
            self._screenshot_manager = SeleniumScreenshotManager(self._driver)
        else:  # PLAYWRIGHT
            from framework.waiter import PlaywrightWaitManager
            from framework.screenshot import PlaywrightScreenshotManager

            self._wait_manager = PlaywrightWaitManager(self._driver, self._timeout)
            self._screenshot_manager = PlaywrightScreenshotManager(self._driver)

    @log_action("Finding element")
    def find(self) -> Optional[Any]:
        """Find element"""
        if self._driver_type == DriverType.SELENIUM:
            selenium_locator = self._locator.to_selenium()
            return self._wait_manager.wait_for_presence(selenium_locator, self._timeout)
        else:  # PLAYWRIGHT
            playwright_locator = self._locator.to_playwright()
            return self._wait_manager.wait_for_presence(
                playwright_locator, self._timeout
            )

    @log_action("Checking if clickable")
    def is_clickable(self) -> bool:
        """Check if element is clickable"""
        if self._driver_type == DriverType.SELENIUM:
            selenium_locator = self._locator.to_selenium()
            element = self._wait_manager.wait_for_clickable(
                selenium_locator, timeout=100
            )
        else:
            playwright_locator = self._locator.to_playwright()
            element = self._wait_manager.wait_for_clickable(
                playwright_locator, timeout=100
            )
        return element is not None

    @log_action("Checking if visible")
    def is_visible(self) -> bool:
        """Check if element is visible"""
        element = self.find()
        if element is None:
            return False

        if self._driver_type == DriverType.SELENIUM:
            return element.is_displayed()
        else:
            return element.is_visible()

    @log_action("Checking if presented")
    def is_presented(self) -> bool:
        """Check if element is present on page"""
        return self.find() is not None

    @log_action("Performing click")
    def click(self, x_offset: int = 0, y_offset: int = 0):
        """Click element"""
        element = self.find()

        if not element:
            raise ElementNotFound(f"Element {self._locator} not found")

        if self._driver_type == DriverType.SELENIUM:
            from framework.actions import SeleniumElementActions

            actions = SeleniumElementActions(self._driver, element)
        else:
            from framework.actions import PlaywrightElementActions

            actions = PlaywrightElementActions(self._driver, element)

        actions.click(x_offset, y_offset)

    @log_action("Sending keys")
    def send_keys(self, text: str):
        """Type text into element"""
        element = self.find()

        if not element:
            raise ElementNotFound(f"Element {self._locator} not found")

        if self._driver_type == DriverType.SELENIUM:
            from framework.actions import SeleniumElementActions

            actions = SeleniumElementActions(self._driver, element)
        else:
            from framework.actions import PlaywrightElementActions

            actions = PlaywrightElementActions(self._driver, element)

        actions.send_keys(text)

    @log_action("Getting text")
    def get_text(self) -> str:
        """Get element text"""
        element = self.find()

        if not element:
            return ""

        if self._driver_type == DriverType.SELENIUM:
            from framework.actions import SeleniumElementActions

            actions = SeleniumElementActions(self._driver, element)
        else:
            from framework.actions import PlaywrightElementActions

            actions = PlaywrightElementActions(self._driver, element)

        return actions.get_text()

    @log_action("Getting attribute")
    def get_attribute(self, attr_name: str) -> Optional[str]:
        """Get element attribute"""
        element = self.find()

        if not element:
            return None

        if self._driver_type == DriverType.SELENIUM:
            from framework.actions import SeleniumElementActions

            actions = SeleniumElementActions(self._driver, element)
        else:
            from framework.actions import PlaywrightElementActions

            actions = PlaywrightElementActions(self._driver, element)

        return actions.get_attribute(attr_name)

    @log_action("Taking screenshot")
    def highlight_and_screenshot(self, file_name: str = "element.png"):
        """Highlight element with red border and take screenshot"""
        element = self.find()
        if element:
            self._screenshot_manager.highlight_and_screenshot(element, file_name)


class ManyWebElements(WebElement):
    """Collection of elements"""

    @log_action("Finding elements")
    def find(self) -> List[Any]:
        """Find multiple elements"""
        if self._driver_type == DriverType.SELENIUM:
            selenium_locator = self._locator.to_selenium()
            try:
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC

                wait = WebDriverWait(self._driver, self._timeout / 1000)
                return wait.until(EC.presence_of_all_elements_located(selenium_locator))
            except Exception as e:
                self._logger.warning(f"Find many failed: {e}")
                return []
        else:
            playwright_locator = self._locator.to_playwright()
            try:
                return self._driver.locator(playwright_locator).all()
            except Exception as e:
                self._logger.warning(f"Find many failed: {e}")
                return []

    @log_action("Counting elements")
    def count(self) -> int:
        """Get count of elements"""
        elements = self.find()
        return len(elements)

    @log_action("Getting all text")
    def get_all_text(self) -> List[str]:
        """Get text from all elements"""
        elements = self.find()

        if self._driver_type == DriverType.SELENIUM:
            return [elem.text or "" for elem in elements]
        else:
            return [elem.text_content() or "" for elem in elements]

    def __getitem__(self, index: int):
        """Access element by index"""
        elements = self.find()
        return elements[index]


class ElementNotFound(Exception):
    """Custom exception for element not found"""

    pass
