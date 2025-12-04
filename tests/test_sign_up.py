from pages.signup_actions import SignupPageActions


def test_signup_positive(
    signup_page: SignupPageActions,
):
    # Check if page is displayed
    assert signup_page.is_page_displayed(), "Sign up page not displayed"