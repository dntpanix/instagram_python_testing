from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class LocatorType(Enum):
    XPATH = "xpath"
    CSS = "css"
    ID = "id"
    TEXT = "text"


class DriverType(Enum):
    SELENIUM = "selenium"
    PLAYWRIGHT = "playwright"


@dataclass
class Locator:
    """Type-safe locator abstraction"""

    type: LocatorType
    value: str

    def to_selenium(self) -> Tuple[str, str]:
        """Convert to Selenium format"""
        from selenium.webdriver.common.by import By

        mapping = {
            LocatorType.XPATH: By.XPATH,
            LocatorType.CSS: By.CSS_SELECTOR,
            LocatorType.ID: By.ID,
        }
        return (mapping[self.type], self.value)

    def to_playwright(self) -> str:
        """Convert to Playwright format"""
        mapping = {
            LocatorType.XPATH: lambda v: v,  # Playwright supports xpath directly
            LocatorType.CSS: lambda v: v,  # CSS selector format
            LocatorType.ID: lambda v: f"#{v}",
            LocatorType.TEXT: lambda v: f"text={v}",
        }
        converter = mapping.get(self.type, lambda v: v)
        return converter(self.value)
