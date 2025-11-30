from framework.driver_factory import DriverFactory
from framework.locator import DriverType
from pages.login import LoginPage
from pages.login_actions import LoginPageActions


def test_try_pw():
    # Create Playwright browser
    context, browser, playwright = DriverFactory.create_playwright_local(
        browser_type="chromium",
        headless=False
    )
    page = context.new_page()

    try:
        # Navigate to login page
        page.goto("http://localhost:5001/login/")
        
        # Create page object
        l_page = LoginPage(page, DriverType.PLAYWRIGHT)
        login_page = LoginPageActions(l_page)
        
        # Check if page is displayed
        # assert login_page.is_page_displayed(), "Login page not displayed"
        
        # Check individual elements
        assert login_page.is_username_input_visible(), "Username input not visible"
        assert login_page.is_password_input_visible(), "Password input not visible"
        
        # Perform login
        login_page.login("themepark", "password123")
        
        # Wait for redirect
        page.wait_for_load_state("networkidle")
        
    finally:
        context.close()
        browser.close()
        playwright.stop()