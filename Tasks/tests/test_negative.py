from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login(driver):

    page = LoginPage(driver)

    page.open()

    page.login(
        "wrong@gmail.com",
        "123456"
    )

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "invalid-feedback")
        )
    )

    assert error.is_displayed()