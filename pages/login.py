from dataclasses import dataclass
from framework.locator import Locator, LocatorType, DriverType
from framework.element import WebElement
from framework.logger import setup_logger, log_action


@dataclass
class LoginPageLocators:
    """All locators for the login page"""

    # Main form
    LOGIN_FORM = Locator(
        type=LocatorType.XPATH,
        value='//article/div[@class="x5n08af x78zum5 xdt5ytf x1iyjqo2 xl56j7k x7qam4e x14vqqas x15lw1kp x1dc814f x1owpceq xh8yej3"]',
    )

    # Input fields
    USERNAME_INPUT = Locator(type=LocatorType.XPATH, value="//input[@name='username']")

    PASSWORD_INPUT = Locator(type=LocatorType.XPATH, value="//input[@name='password']")

    # Buttons
    LOGIN_BUTTON = Locator(type=LocatorType.XPATH, value="//button[@type='submit']")

    FACEBOOK_LOGIN_BUTTON = Locator(
        type=LocatorType.XPATH,
        value="//button[@type='button' and contains(.//text(), 'Log in with Facebook')]",
    )

    # Links
    FORGOT_PASSWORD_LINK = Locator(
        type=LocatorType.XPATH,
        value="//a[@href='/accounts/password/reset/' and contains(text(), 'Forgot password?')]",
    )

    SIGN_UP_LINK = Locator(
        type=LocatorType.XPATH,
        value="//a[@href='/accounts/emailsignup/' and contains(.//text(), 'Sign up')]",
    )

    # Error message
    ERROR_MESSAGE = Locator(type=LocatorType.ID, value="error-message")

    # Logo
    LOGO_IMAGE = Locator(type=LocatorType.XPATH, value="//i[@aria-label='Instagram']")


class LoginPage:
    """Page Object Model for Login Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        """
        Initialize LoginPage

        Args:
            driver: Selenium WebDriver or Playwright Page instance
            driver_type: Type of driver (SELENIUM or PLAYWRIGHT)
            timeout: Timeout in milliseconds for element waits
        """
        if driver_type == DriverType.SELENIUM:
            if not hasattr(driver, "find_element"):
                raise TypeError(
                    f"Expected Selenium WebDriver, got {type(driver).__name__}. "
                    f"Pass a WebDriver instance for DriverType.SELENIUM"
                )
        else:  # PLAYWRIGHT
            if not hasattr(driver, "locator"):
                raise TypeError(
                    f"Expected Playwright Page, got {type(driver).__name__}. "
                    f"Pass a Page instance for DriverType.PLAYWRIGHT"
                )
        self._driver = driver
        self._driver_type = driver_type
        self._timeout = timeout
        self._logger = setup_logger(self.__class__.__name__)
        self._locators = LoginPageLocators()

    # Elements as properties
    @property
    def login_form(self) -> WebElement:
        """Get login form element"""
        return WebElement(
            self._locators.LOGIN_FORM, self._driver, self._driver_type, self._timeout
        )

    @property
    def username_input(self) -> WebElement:
        """Get username input element"""
        return WebElement(
            self._locators.USERNAME_INPUT,
            self._driver,
            self._driver_type,
            self._timeout,
        )

    @property
    def password_input(self) -> WebElement:
        """Get password input element"""
        return WebElement(
            self._locators.PASSWORD_INPUT,
            self._driver,
            self._driver_type,
            self._timeout,
        )

    @property
    def login_button(self) -> WebElement:
        """Get login button element"""
        return WebElement(
            self._locators.LOGIN_BUTTON, self._driver, self._driver_type, self._timeout
        )

    @property
    def facebook_login_button(self) -> WebElement:
        """Get Facebook login button element"""
        return WebElement(
            self._locators.FACEBOOK_LOGIN_BUTTON,
            self._driver,
            self._driver_type,
            self._timeout,
        )

    @property
    def forgot_password_link(self) -> WebElement:
        """Get forgot password link element"""
        return WebElement(
            self._locators.FORGOT_PASSWORD_LINK,
            self._driver,
            self._driver_type,
            self._timeout,
        )

    @property
    def sign_up_link(self) -> WebElement:
        """Get sign up link element"""
        return WebElement(
            self._locators.SIGN_UP_LINK, self._driver, self._driver_type, self._timeout
        )

    @property
    def error_message(self) -> WebElement:
        """Get error message element"""
        return WebElement(
            self._locators.ERROR_MESSAGE, self._driver, self._driver_type, self._timeout
        )

    @property
    def logo_image(self) -> WebElement:
        """Get logo image element"""
        return WebElement(
            self._locators.LOGO_IMAGE, self._driver, self._driver_type, self._timeout
        )

    # Page state checks
    @log_action("Checking if login page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        try:
            return (
                self.login_form.is_presented()
                and self.username_input.is_presented()
                and self.password_input.is_presented()
                and self.login_button.is_presented()
            )
        except Exception as e:
            self._logger.error(f"Failed to check if page displayed: {e}")
            return False

    @log_action("Checking if username input is visible")
    def is_username_input_visible(self) -> bool:
        """Check if username input is visible"""
        try:
            return self.username_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check username visibility: {e}")
            return False

    @log_action("Checking if password input is visible")
    def is_password_input_visible(self) -> bool:
        """Check if password input is visible"""
        try:
            return self.password_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password visibility: {e}")
            return False

    @log_action("Checking if login button is clickable")
    def is_login_button_clickable(self) -> bool:
        """Check if login button is clickable"""
        try:
            return self.login_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check login button clickability: {e}")
            return False

    @log_action("Getting error message")
    def get_error_message(self) -> str:
        """Get error message text if displayed"""
        try:
            if self.error_message.is_visible():
                message = self.error_message.get_text()
                self._logger.warning(f"Error message: {message}")
                return message
            return None
        except Exception as e:
            self._logger.error(f"Failed to get error message: {e}")
            return None

    @log_action("Checking if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed"""
        try:
            return self.error_message.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check error message: {e}")
            return False

    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "login_page.png") -> None:
        """Take a screenshot of the login page"""
        try:
            self.login_form.highlight_and_screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")
