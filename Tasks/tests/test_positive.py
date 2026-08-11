from pages.login_page import LoginPage

USERNAME = "your_email"
PASSWORD = "your_password"


def test_guvi_login(driver):

    page = LoginPage(driver)

    page.open()

    assert driver.current_url.startswith(LoginPage.LOGIN_URL)

    assert driver.find_element(*page.EMAIL).is_displayed()
    assert driver.find_element(*page.PASSWORD).is_displayed()

    assert driver.find_element(*page.EMAIL).is_enabled()
    assert driver.find_element(*page.PASSWORD).is_enabled()

    page.login(USERNAME, PASSWORD)

    # Successful login should leave the sign-in page
    assert "sign-in" in driver.current_url