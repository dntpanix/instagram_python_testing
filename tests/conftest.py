import pytest

from framework.driver_factory import DriverFactory
from framework.locator import DriverType
from pages.login import LoginPage
from pages.login_actions import LoginPageActions


DEBUG_URL = "http://localhost:5000/"
TEST_URL = "https://www.instagram.com/"
DEBUG = True

@pytest.fixture(scope="session")
def login_page():
    """Fixture to provide LoginPageActions instance"""
    headless = not DEBUG
    url = DEBUG_URL if DEBUG else TEST_URL
    context, browser, playwright = DriverFactory.create_playwright_local(
        browser_type="chromium", headless=headless
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