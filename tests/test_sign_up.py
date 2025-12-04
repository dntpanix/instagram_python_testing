from pages.signup_actions import SignupPageActions


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
    assert signup_page.is_password_confirm_input_visible(), "Password confirmation input should be visible"

    """Test that signup button is visible"""
    assert signup_page._page.is_signup_button_visible(), "Signup button should be visible"

    """Test that landing image is visible"""
    assert signup_page.is_landing_image_visible(), "Landing image should be visible"

    """Test that description text exists"""
    description = signup_page.get_description_text()
    assert description is not None, "Description text should exist"
    assert len(description) > 0, "Description text should not be empty"
