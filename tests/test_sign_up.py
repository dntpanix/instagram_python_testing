import time
from pages.signup_actions import SignupPageActions
from pages.login_actions import LoginPageActions


def test_signup_page_is_displayed(signup_page: SignupPageActions):
    """Test that signup page loads and is displayed"""
    assert signup_page.is_page_displayed(), "Signup page should be displayed"


def test_all_form_elements_visible(signup_page: SignupPageActions):
    """Test that email input is visible"""
    assert signup_page.is_email_input_visible(), "Email input should be visible"

    """Test that username input is visible"""
    assert signup_page.is_username_input_visible(), "Username input should be visible"

    """Test that password input is visible"""
    assert signup_page.is_password_input_visible(), "Password input should be visible"

    """Test that password confirmation input is visible"""
    assert (
        signup_page.is_password_confirm_input_visible()
    ), "Password confirmation input should be visible"

    """Test that signup button is visible"""
    assert (
        signup_page._page.is_signup_button_visible()
    ), "Signup button should be visible"

    """Test that landing image is visible"""
    assert signup_page.is_landing_image_visible(), "Landing image should be visible"

    """Test that description text exists"""
    description = signup_page.get_description_text()
    assert description is not None, "Description text should exist"
    assert len(description) > 0, "Description text should not be empty"


def test_signup_with_valid_credentials(
    signup_page: SignupPageActions, login_page: LoginPageActions
):
    """Test signup with valid credentials"""
    timestamp = int(time.time())
    email = f"user{timestamp}@test.com"
    username = f"user{timestamp}"
    password = "ValidPass123!"

    result = signup_page.signup(
        email=email, username=username, password=password, password_confirm=password
    )

    assert result is True, "Signup should succeed with valid credentials"

    login_page.login(username, password)

    # Wait for redirect
    assert not login_page._page.login_form.is_visible(), "Login form still displayed"


def test_signup_with_existing_username(
    signup_page: SignupPageActions, get_test_credentials: tuple[str, str]
):
    """Test signup with an existing username"""
    signup_page._page._driver.goto("http://localhost:5000/accounts/emailsignup/")
    existing_username, _ = get_test_credentials
    email = f"newuser{int(time.time())}@test.com"
    password = "ValidPass123!"

    result = signup_page.signup(
        email=email,
        username=existing_username,
        password=password,
        password_confirm=password,
    )
    assert result is False, "Signup should fail with existing username"

    error_message = signup_page.get_error_message()
    assert (
        "username already taken" in error_message.lower()
    ), "Error message should indicate username is taken"
