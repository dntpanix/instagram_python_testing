"""Abstraction layer for waiting - supports both Selenium and Playwright"""

from typing import Optional, Any
from abc import ABC, abstractmethod
from framework.logger import setup_logger


class BaseWaitManager(ABC):
    """Abstract wait manager interface"""

    @abstractmethod
    def wait_for_presence(
        self, locator, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element presence"""
        pass

    @abstractmethod
    def wait_for_clickable(
        self, locator, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be clickable"""
        pass

    @abstractmethod
    def wait_for_visibility(
        self, locator, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element visibility"""
        pass


class SeleniumWaitManager(BaseWaitManager):
    """Selenium wait implementation"""

    def __init__(self, driver, timeout: int = 10000):
        self.driver = driver
        self.timeout = timeout
        self.logger = setup_logger(self.__class__.__name__)

    def wait_for_presence(
        self, locator_tuple, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element presence"""
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            actual_timeout = (timeout or self.timeout) / 1000
            wait = WebDriverWait(self.driver, actual_timeout)
            return wait.until(
                EC.presence_of_element_located(locator_tuple),
                message=f"Element {locator_tuple} not found",
            )
        except Exception as e:
            self.logger.warning(f"Wait for presence failed: {e}")
            return None

    def wait_for_clickable(
        self, locator_tuple, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be clickable"""
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            actual_timeout = (timeout or self.timeout) / 1000
            wait = WebDriverWait(self.driver, actual_timeout)
            return wait.until(
                EC.element_to_be_clickable(locator_tuple),
                message=f"Element {locator_tuple} not clickable",
            )
        except Exception as e:
            self.logger.warning(f"Wait for clickable failed: {e}")
            return None

    def wait_for_visibility(
        self, locator_tuple, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element visibility"""
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            actual_timeout = (timeout or self.timeout) / 1000
            wait = WebDriverWait(self.driver, actual_timeout)
            return wait.until(
                EC.visibility_of_element_located(locator_tuple),
                message=f"Element {locator_tuple} not visible",
            )
        except Exception as e:
            self.logger.warning(f"Wait for visibility failed: {e}")
            return None


class PlaywrightWaitManager(BaseWaitManager):
    """Playwright wait implementation"""

    def __init__(self, page, timeout: int = 10000):
        self.page = page
        self.timeout = timeout
        self.logger = setup_logger(self.__class__.__name__)

    def wait_for_presence(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element presence"""
        try:
            actual_timeout = timeout or self.timeout
            self.page.wait_for_selector(locator, timeout=actual_timeout)
            return self.page.locator(locator)
        except Exception as e:
            self.logger.warning(f"Wait for presence failed: {e}")
            return None

    def wait_for_clickable(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be clickable"""
        try:
            actual_timeout = timeout or self.timeout
            locator_obj = self.page.locator(locator)
            locator_obj.wait_for(state="visible", timeout=actual_timeout)
            return locator_obj
        except Exception as e:
            self.logger.warning(f"Wait for clickable failed: {e}")
            return None

    def wait_for_visibility(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element visibility"""
        try:
            actual_timeout = timeout or self.timeout
            locator_obj = self.page.locator(locator)
            locator_obj.wait_for(state="visible", timeout=actual_timeout)
            return locator_obj
        except Exception as e:
            self.logger.warning(f"Wait for visibility failed: {e}")
            return None
