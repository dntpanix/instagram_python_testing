from pages.login_actions import LoginPageActions


def test_login_positive(
    login_page: LoginPageActions,
    get_test_credentials: tuple[str, str],
):
    # Check if page is displayed
    assert login_page.is_page_displayed(), "Login page not displayed"

    # Check individual elements
    assert login_page.is_username_input_visible(), "Username input not visible"
    assert login_page.is_password_input_visible(), "Password input not visible"

    # Perform login
    login, password = get_test_credentials
    login_page.login(login, password)

    # Wait for redirect
    assert not login_page._page.login_form.is_visible(), "Login form still displayed"
    