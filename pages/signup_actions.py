import time
from framework.logger import log_action, setup_logger
from pages.signup import SignupPage


class SignupPageActions:

    def __init__(self, signup_page: SignupPage):
        """
        Initialize SignupPageActions with a SignupPage instance

        Args:
            signup_page: SignupPage object instance
        """
        if not isinstance(signup_page, type(signup_page)):
            # Just check it has the expected methods
            required_methods = [
                "is_email_input_visible",
                "is_username_input_visible",
                "is_password_input_visible",
                "is_password_confirm_input_visible",
                "email_input",
                "username_input",
                "password_input",
                "password_confirm_input",
                "signup_button",
                "error_message",
            ]
            for method in required_methods:
                if not hasattr(signup_page, method):
                    raise AttributeError(f"SignupPage must have '{method}' attribute")

        self._page = signup_page
        self._logger = setup_logger(self.__class__.__name__)

    @log_action("Performing signup")
    def signup(
        self,
        email: str,
        username: str,
        password: str,
        password_confirm: str,
        wait_after_signup: float = 2.0,
    ) -> bool:
        """
        Perform signup with email, username, and password

        Args:
            email: Email address
            username: Username
            password: Password
            password_confirm: Password confirmation
            wait_after_signup: Time to wait after clicking signup button (seconds)

        Returns:
            True if signup was successful, False otherwise

        Raises:
            Exception: If signup fails with details
        """
        try:
            self._logger.info(f"Starting signup with email: {email}, username: {username}")

            # Check if inputs are visible
            if not self._page.is_email_input_visible():
                raise AssertionError("Email input not visible")

            if not self._page.is_username_input_visible():
                raise AssertionError("Username input not visible")

            if not self._page.is_password_input_visible():
                raise AssertionError("Password input not visible")

            if not self._page.is_password_confirm_input_visible():
                raise AssertionError("Password confirmation input not visible")

            # Enter credentials
            self._logger.debug("Entering email")
            self._page.email_input.send_keys(email)

            self._logger.debug("Entering username")
            self._page.username_input.send_keys(username)

            self._logger.debug("Entering password")
            self._page.password_input.send_keys(password)

            self._logger.debug("Entering password confirmation")
            self._page.password_confirm_input.send_keys(password_confirm)

            # Click signup button
            self._logger.debug("Clicking signup button")
            self._page.signup_button.click()

            # Wait for page to process signup
            time.sleep(wait_after_signup)

            self._logger.info("Signup fill successfully")
            return not self._page.is_error_message_displayed()  # Assuming redirect on success

        except Exception as e:
            self._logger.error(f"Signup failed: {type(e).__name__}: {str(e)}")
            raise

    @log_action("Entering email")
    def enter_email(self, email: str) -> None:
        """
        Enter email without other fields

        Args:
            email: Email address to enter
        """
        try:
            if not self._page.is_email_input_visible():
                raise AssertionError("Email input not visible")

            self._logger.debug(f"Entering email: {email}")
            self._page.email_input.send_keys(email)

        except Exception as e:
            self._logger.error(f"Failed to enter email: {e}")
            raise

    @log_action("Entering username")
    def enter_username(self, username: str) -> None:
        """
        Enter username without other fields

        Args:
            username: Username to enter
        """
        try:
            if not self._page.is_username_input_visible():
                raise AssertionError("Username input not visible")

            self._logger.debug(f"Entering username: {username}")
            self._page.username_input.send_keys(username)

        except Exception as e:
            self._logger.error(f"Failed to enter username: {e}")
            raise

    @log_action("Entering password")
    def enter_password(self, password: str) -> None:
        """
        Enter password without other fields

        Args:
            password: Password to enter
        """
        try:
            if not self._page.is_password_input_visible():
                raise AssertionError("Password input not visible")

            self._logger.debug("Entering password")
            self._page.password_input.send_keys(password)

        except Exception as e:
            self._logger.error(f"Failed to enter password: {e}")
            raise

    @log_action("Entering password confirmation")
    def enter_password_confirm(self, password_confirm: str) -> None:
        """
        Enter password confirmation without other fields

        Args:
            password_confirm: Password confirmation to enter
        """
        try:
            if not self._page.is_password_confirm_input_visible():
                raise AssertionError("Password confirmation input not visible")

            self._logger.debug("Entering password confirmation")
            self._page.password_confirm_input.send_keys(password_confirm)

        except Exception as e:
            self._logger.error(f"Failed to enter password confirmation: {e}")
            raise

    @log_action("Clicking signup button")
    def click_signup_button(self) -> None:
        """Click the signup button"""
        try:
            if not self._page.is_signup_button_clickable():
                raise AssertionError("Signup button not clickable")

            self._logger.debug("Clicking signup button")
            self._page.signup_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click signup button: {e}")
            raise

    @log_action("Checking if email input is visible")
    def is_email_input_visible(self) -> bool:
        """Check if email input is visible"""
        try:
            return self._page.is_email_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check email visibility: {e}")
            return False

    @log_action("Checking if username input is visible")
    def is_username_input_visible(self) -> bool:
        """Check if username input is visible"""
        try:
            return self._page.is_username_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check username visibility: {e}")
            return False

    @log_action("Checking if password input is visible")
    def is_password_input_visible(self) -> bool:
        """Check if password input is visible"""
        try:
            return self._page.is_password_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password visibility: {e}")
            return False

    @log_action("Checking if password confirmation input is visible")
    def is_password_confirm_input_visible(self) -> bool:
        """Check if password confirmation input is visible"""
        try:
            return self._page.is_password_confirm_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password confirmation visibility: {e}")
            return False

    @log_action("Checking if signup page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if signup page is displayed"""
        try:
            return self._page.is_page_displayed()
        except Exception as e:
            self._logger.error(f"Failed to check page display: {e}")
            return False

    @log_action("Checking if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed"""
        try:
            return self._page.is_error_message_displayed()
        except Exception as e:
            self._logger.error(f"Failed to check error message: {e}")
            return False

    @log_action("Getting error message")
    def get_error_message(self) -> str:
        """Get error message text if displayed"""
        try:
            return self._page.get_error_message()
        except Exception as e:
            self._logger.error(f"Failed to get error message: {e}")
            return None

    @log_action("Clicking login link")
    def click_login_link(self) -> None:
        """Click the login link"""
        try:
            self._logger.debug("Clicking login link")
            self._page.login_link.click()

        except Exception as e:
            self._logger.error(f"Failed to click login link: {e}")
            raise

    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "signup_page.png") -> None:
        """Take a screenshot of the signup page"""
        try:
            self._page.screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")
            raise

    @log_action("Validating signup form")
    def validate_signup_form(self) -> bool:
        """
        Validate that all signup form elements are present and visible

        Returns:
            True if all elements are valid, False otherwise
        """
        try:
            checks = {
                "Email input visible": self._page.is_email_input_visible(),
                "Username input visible": self._page.is_username_input_visible(),
                "Password input visible": self._page.is_password_input_visible(),
                "Password confirmation input visible": self._page.is_password_confirm_input_visible(),
                "Signup button visible": self._page.is_signup_button_visible(),
            }

            all_valid = all(checks.values())

            for check_name, result in checks.items():
                status = "✓" if result else "✗"
                self._logger.info(f"{status} {check_name}: {result}")

            return all_valid

        except Exception as e:
            self._logger.error(f"Validation failed: {e}")
            return False

    @log_action("Checking if landing image is visible")
    def is_landing_image_visible(self) -> bool:
        """Check if landing image is visible"""
        try:
            return self._page.is_landing_image_visible()
        except Exception as e:
            self._logger.error(f"Failed to check landing image visibility: {e}")
            return False

    @log_action("Getting description text")
    def get_description_text(self) -> str:
        """Get description text"""
        try:
            return self._page.get_description_text()
        except Exception as e:
            self._logger.error(f"Failed to get description text: {e}")
            return None
