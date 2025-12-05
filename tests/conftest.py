import os
import pytest
from contextlib import contextmanager

from framework.driver_factory import DriverFactory
from framework.locator import DriverType

from pages.login import LoginPage
from pages.login_actions import LoginPageActions
from pages.signup import SignupPage
from pages.signup_actions import SignupPageActions

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
    """Context manager to create and cleanup browser context"""
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


@pytest.fixture(scope="module")
def base_page():
    """Base fixture that provides page object and URL"""
    url = DEBUG_URL if DEBUG else TEST_URL
    with build_context(url) as page:
        yield url, page


@pytest.fixture()
def login_page(base_page):
    """fixture for login page"""
    url, page = base_page
    login_page = LoginPage(page, DriverType.PLAYWRIGHT)
    login_page_actions = LoginPageActions(login_page)
    yield login_page_actions
    logout(url, login_page_actions)


@pytest.fixture(scope="module")
def signup_page(base_page):
    """fixture for signup page"""
    url, page = base_page
    # Navigate to signup URL
    signup_url = f"{url}/accounts/emailsignup/"
    page.goto(signup_url)
    
    # Create page objects
    signup_page = SignupPage(page, DriverType.PLAYWRIGHT)
    signup_page_actions = SignupPageActions(signup_page)
    
    yield signup_page_actions
    logout(url, signup_page_actions)
