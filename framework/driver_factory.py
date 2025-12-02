from framework.logger import log_waning
try:
    from selenium import webdriver
except ImportError:
    log_waning("Selenium not installed, Selenium webdriver will not work")
try:    
    from playwright.sync_api import sync_playwright
except ImportError:
    log_waning("Playwright not installed, Playwright browser factory will not work")


class DriverFactory:
    """Factory for creating driver instances"""

    @staticmethod
    def create_selenium_local(browser: str = "firefox", headless: bool = True):
        """Create local Selenium driver"""

        options = {
            "firefox": webdriver.FirefoxOptions,
            "chrome": webdriver.ChromeOptions,
        }.get(browser)()

        if headless:
            options.add_argument("--headless")
        if browser == "firefox":
            return webdriver.Firefox(options=options)
        elif browser == "chrome":
            return webdriver.Chrome(options=options)

    @staticmethod
    def create_selenium_remote(
        command_executor: str, desired_capabilities: dict, timeout: int = 30
    ):
        """Create remote Selenium driver"""

        return webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=desired_capabilities,
            timeout=timeout,
        )

    @staticmethod
    def create_playwright_local(
        browser_type: str = "chromium", headless: bool = True, timeout: int = 30000
    ):
        """Create local Playwright browser"""

        p = sync_playwright().start()

        browser_map = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit,
        }

        browser = browser_map[browser_type].launch(headless=headless)
        return browser.new_context(), browser, p

    @staticmethod
    def create_playwright_remote(
        ws_endpoint: str, browser_type: str = "chromium", timeout: int = 30000
    ):
        """Create remote Playwright browser via WebSocket"""

        p = sync_playwright().start()

        browser_map = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit,
        }

        browser = browser_map[browser_type].connect(ws_endpoint, timeout=timeout)
        return browser.new_context(), browser, p
