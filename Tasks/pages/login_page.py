from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    LOGIN_URL = "https://www.guvi.in/sign-in/"

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-btn")

    # Cookie popup buttons
    GOT_IT = (By.XPATH, "//button[normalize-space()='Got it!']")
    DENY_COOKIES = (By.XPATH, "//button[normalize-space()='Deny cookies']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.LOGIN_URL)

        # Handle cookie popup
        self.handle_cookies()

    def handle_cookies(self):
        try:
            got_it = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.GOT_IT)
            )
            got_it.click()

        except TimeoutException:
            try:
                deny_cookies = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable(self.DENY_COOKIES)
                )
                deny_cookies.click()

            except TimeoutException:
                # Cookie popup was not displayed
                pass

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN)
        ).click()