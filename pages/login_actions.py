from pages.login import LoginPage
from framework.locator import DriverType
from framework.logger import log_action

class LoginPageActions(LoginPage):

    @log_action("Checking if login page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        return (
            self.login_form.is_presented() and
            self.username_input.is_presented() and
            self.password_input.is_presented() and
            self.login_button.is_presented()
        )
    
    @log_action("Performing login")
    def login(self, username: str, password: str) -> None:
        """
        Perform login with username and password
        
        Args:
            username: Username or email
            password: Password
            
        Raises:
            Exception: If login fails
        """
        try:
            self._logger.info(f"Attempting login with username: {username}")
            
            # Clear and fill username
            self.username_input.send_keys(username)
            self._logger.debug("Username entered successfully")
            
            # Clear and fill password
            self.password_input.send_keys(password)
            self._logger.debug("Password entered successfully")
            
            # Click login button
            self.login_button.click()
            self._logger.info("Login button clicked successfully")
            
        except Exception as e:
            self._logger.error(f"Login failed: {str(e)}")
            raise
    
    @log_action("Entering username")
    def enter_username(self, username: str) -> None:
        """
        Enter username in the username field
        
        Args:
            username: Username or email to enter
        """
        self.username_input.send_keys(username)
        self._logger.debug(f"Username entered: {username}")
    
    @log_action("Entering password")
    def enter_password(self, password: str) -> None:
        """
        Enter password in the password field
        
        Args:
            password: Password to enter
        """
        self.password_input.send_keys(password)
        self._logger.debug("Password entered")
    
    @log_action("Clicking login button")
    def click_login_button(self) -> None:
        """Click the login button"""
        self.login_button.click()
        self._logger.debug("Login button clicked")
    
    @log_action("Getting error message")
    def get_error_message(self) -> str:
        """
        Get error message text if displayed
        
        Returns:
            Error message text or None if not displayed
        """
        if self.error_message.is_visible():
            message = self.error_message.get_text()
            self._logger.warning(f"Error message displayed: {message}")
            return message
        return None
    
    @log_action("Checking if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        """
        Check if error message is displayed
        
        Returns:
            True if error message is visible, False otherwise
        """
        return self.error_message.is_visible()
    
    @log_action("Clicking forgot password link")
    def click_forgot_password(self) -> None:
        """Click the forgot password link"""
        self.forgot_password_link.click()
        self._logger.debug("Forgot password link clicked")
    
    @log_action("Clicking sign up link")
    def click_sign_up(self) -> None:
        """Click the sign up link"""
        self.sign_up_link.click()
        self._logger.debug("Sign up link clicked")
    
    @log_action("Clicking Facebook login button")
    def click_facebook_login(self) -> None:
        """Click the Facebook login button"""
        self.facebook_login_button.click()
        self._logger.debug("Facebook login button clicked")
    
    @log_action("Checking if username input is visible")
    def is_username_input_visible(self) -> bool:
        """Check if username input is visible"""
        return self.username_input.is_visible()
    
    @log_action("Checking if password input is visible")
    def is_password_input_visible(self) -> bool:
        """Check if password input is visible"""
        return self.password_input.is_visible()
    
    @log_action("Getting username value")
    def get_username_value(self) -> str:
        """Get the current value of username input"""
        return self.username_input.get_text()
    
    @log_action("Clearing username input")
    def clear_username(self) -> None:
        """Clear the username input field"""
        username_elem = self.username_input.find()
        if username_elem:
            if self._driver_type == DriverType.SELENIUM:
                username_elem.clear()
            else:  # PLAYWRIGHT
                username_elem.clear()
            self._logger.debug("Username field cleared")
    
    @log_action("Clearing password input")
    def clear_password(self) -> None:
        """Clear the password input field"""
        password_elem = self.password_input.find()
        if password_elem:
            if self._driver_type == DriverType.SELENIUM:
                password_elem.clear()
            else:  # PLAYWRIGHT
                password_elem.clear()
            self._logger.debug("Password field cleared")
    
    @log_action("Checking if login button is clickable")
    def is_login_button_clickable(self) -> bool:
        """Check if login button is clickable"""
        return self.login_button.is_clickable()
    
    @log_action("Taking login page screenshot")
    def screenshot(self, file_name: str = 'login_page.png') -> None:
        """
        Take a screenshot of the login page
        
        Args:
            file_name: Name of the screenshot file
        """
        self.login_form.highlight_and_screenshot(file_name)
        self._logger.debug(f"Screenshot saved: {file_name}")
