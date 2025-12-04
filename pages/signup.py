from dataclasses import dataclass
from framework.locator import Locator, LocatorType, DriverType
from framework.element import element, WebElement
from framework.logger import log_action
from pages._base import BasePage

@dataclass
class SignupPageLocators:
    """All locators for the signup page"""

    # Main form
    SIGNUP_FORM = Locator(
        type=LocatorType.ID,
        value='signupForm',
    )

    # Input fields
    EMAIL_INPUT = Locator(
        type=LocatorType.XPATH, 
        value="//input[@name='email']"
    )

    USERNAME_INPUT = Locator(
        type=LocatorType.XPATH, 
        value="//input[@name='username']"
    )

    PASSWORD_INPUT = Locator(
        type=LocatorType.XPATH, 
        value="//input[@name='password']"
    )

    PASSWORD_CONFIRM_INPUT = Locator(
        type=LocatorType.XPATH, 
        value="//input[@name='password_confirm']"
    )

    # Buttons
    SIGNUP_BUTTON = Locator(
        type=LocatorType.XPATH, 
        value="//button[@type='submit']"
    )

    # Links
    LOGIN_LINK = Locator(
        type=LocatorType.XPATH,
        value="//a[@href='/login' and contains(.//text(), 'Log in')]",
    )

    # Error message
    ERROR_MESSAGE = Locator(
        type=LocatorType.ID, 
        value="error-message"
    )

    # Logo
    LOGO_IMAGE = Locator(
        type=LocatorType.XPATH, 
        value="//i[@aria-label='Instagram']"
    )

    # Landing image
    LANDING_IMAGE = Locator(
        type=LocatorType.XPATH,
        value="//img[contains(@src, 'landing-2x.png')]",
    )

    # Description text
    DESCRIPTION_TEXT = Locator(
        type=LocatorType.XPATH,
        value="//p[contains(text(), 'Sign up to see photos and videos from your friends.')]",
    )


class SignupPage(BasePage):
    """Page Object Model for Signup Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        super().__init__(driver, driver_type, timeout)
        self._locators = SignupPageLocators()

    # Elements as properties
    @element("SIGNUP_FORM")
    def signup_form(self) -> WebElement:
        """Get signup form"""
        pass

    @element("EMAIL_INPUT")
    def email_input(self) -> WebElement:
        """Get email input element"""
        pass

    @element("USERNAME_INPUT")
    def username_input(self) -> WebElement:
        """Get username input element"""
        pass

    @element("PASSWORD_INPUT")
    def password_input(self) -> WebElement:
        """Get password input element"""
        pass

    @element("PASSWORD_CONFIRM_INPUT")
    def password_confirm_input(self) -> WebElement:
        """Get password confirmation input element"""
        pass

    @element("SIGNUP_BUTTON")
    def signup_button(self) -> WebElement:
        """Get signup button element"""
        pass

    @element("LOGIN_LINK")
    def login_link(self) -> WebElement:
        """Get login link element"""
        pass

    @element("ERROR_MESSAGE")
    def error_message(self) -> WebElement:
        """Get error message element"""
        pass

    @element("LOGO_IMAGE")
    def logo_image(self) -> WebElement:
        """Get logo image element"""
        pass

    @element("LANDING_IMAGE")
    def landing_image(self) -> WebElement:
        """Get landing image element"""
        pass

    @element("DESCRIPTION_TEXT")
    def description_text(self) -> WebElement:
        """Get description text element"""
        pass

    # Page state checks
    @log_action("Checking if signup page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if signup page is displayed"""
        try:
            return (
                self.signup_form.is_presented()
                and self.email_input.is_presented()
                and self.username_input.is_presented()
                and self.password_input.is_presented()
                and self.password_confirm_input.is_presented()
                and self.signup_button.is_presented()
            )
        except Exception as e:
            self._logger.error(f"Failed to check if page displayed: {e}")
            return False

    @log_action("Checking if email input is visible")
    def is_email_input_visible(self) -> bool:
        """Check if email input is visible"""
        try:
            return self.email_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check email visibility: {e}")
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

    @log_action("Checking if password confirmation input is visible")
    def is_password_confirm_input_visible(self) -> bool:
        """Check if password confirmation input is visible"""
        try:
            return self.password_confirm_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password confirmation visibility: {e}")
            return False

    @log_action("Checking if signup button is clickable")
    def is_signup_button_clickable(self) -> bool:
        """Check if signup button is clickable"""
        try:
            return self.signup_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check signup button clickability: {e}")
            return False
    
    @log_action("Checking if signup button is visible")
    def is_signup_button_visible(self) -> bool:
        """Check if signup button is clickable"""
        try:
            return self.signup_button.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check signup button clickability: {e}")
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

    @log_action("Checking if landing image is visible")
    def is_landing_image_visible(self) -> bool:
        """Check if landing image is visible"""
        try:
            return self.landing_image.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check landing image visibility: {e}")
            return False

    @log_action("Getting description text")
    def get_description_text(self) -> str:
        """Get description text"""
        try:
            return self.description_text.get_text()
        except Exception as e:
            self._logger.error(f"Failed to get description text: {e}")
            return None

    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "signup_page.png") -> None:
        """Take a screenshot of the signup page"""
        try:
            self.signup_form.highlight_and_screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")
