from pages.login_actions import LoginPageActions


def test_login_positive(login_page: LoginPageActions):
    # Check if page is displayed
    assert login_page.is_page_displayed(), "Login page not displayed"

    # Check individual elements
    assert login_page.is_username_input_visible(), "Username input not visible"
    assert login_page.is_password_input_visible(), "Password input not visible"

    # Perform login
    login_page.login("themepark", "password123")

    # Wait for redirect
    #assert not login_page.is_page_displayed(), "Login page still displayed"