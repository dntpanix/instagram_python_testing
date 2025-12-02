from dataclasses import dataclass
from framework.locator import Locator, LocatorType, DriverType
from framework.element import element, WebElement
from framework.logger import log_action
from pages._base import BasePage

@dataclass
class FeedPageLocators:
    """All locators for the feed page"""

    # Main feed container
    FEED_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//div[@role="main"]',
    )


class FeedPage(BasePage):
    """Page Object Model for Feed Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        super().__init__(driver, driver_type, timeout)
        
        self._locators = FeedPageLocators()

    # Elements as properties
    @element("FEED_CONTAINER")
    def feed_container(self) -> WebElement:
        """Main feed container element"""
        pass
