import os
import pytest

from contextlib import contextmanager
from framework.driver_factory import DriverFactory
from framework.locator import DriverType
from pages.login import LoginPage
from pages.login_actions import LoginPageActions
from tests.helper import logout


DEBUG_URL = os.getenv("DEBUG_URL", "http://localhost:5000/")
TEST_URL = os.getenv("TEST_URL", "https://www.instagram.com/")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


@pytest.fixture(scope="session")
def get_test_credentials() -> tuple[str, str]:
    """Fixture to provide test credentials from environment variables"""
    test_username = os.getenv("TEST_USERNAME", "themepark")
    test_password = os.getenv("TEST_PASSWORD", "password123")
    return test_username, test_password


@contextmanager
def build_context(url: str):
    context, browser, playwright = DriverFactory.create_playwright_local(
        browser_type="chromium", headless=HEADLESS
    )
    page = context.new_page()

    try:
        page.goto(url)
        yield page
    finally:
        context.close()
        browser.close()
        playwright.stop()


@pytest.fixture(scope="session")
def login_page():
    """Fixture to provide LoginPageActions instance"""
    url = DEBUG_URL if DEBUG else TEST_URL
    # Create page object
    with build_context(url) as page:
        login_page = LoginPage(page, DriverType.PLAYWRIGHT)
        login_page_actions = LoginPageActions(login_page)
        yield login_page_actions
        logout(url)
