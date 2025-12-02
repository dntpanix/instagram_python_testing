import os
import pytest

from framework.driver_factory import DriverFactory
from framework.locator import DriverType
from pages.login import LoginPage
from pages.login_actions import LoginPageActions


DEBUG_URL = os.getenv("DEBUG_URL", "http://localhost:5000/login/")
TEST_URL = os.getenv("TEST_URL", "https://www.instagram.com/accounts/login/")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


@pytest.fixture(scope="session")
def login_page():
    """Fixture to provide LoginPageActions instance"""
    url = DEBUG_URL if DEBUG else TEST_URL
    context, browser, playwright = DriverFactory.create_playwright_local(
        browser_type="chromium", headless=HEADLESS
    )
    page = context.new_page()

    try:
        # Navigate to login page
        page.goto(url)

        # Create page object
        l_page = LoginPage(page, DriverType.PLAYWRIGHT)
        login_page = LoginPageActions(l_page)
        yield login_page
    finally:
        context.close()
        browser.close()
        playwright.stop()
