from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # -----------------------------
    # Constructor
    # -----------------------------

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    # -----------------------------
    # Locators
    # -----------------------------

    EMAIL = (By.ID, "«Refvl3ksopa55j6»")

    PASSWORD = (By.ID, "«R2nvl3ksopa55j6»")

    LOGIN_BUTTON = (
    By.XPATH,
    "//button[.//span[normalize-space()='Sign in']]"
    )

    ERROR_MESSAGE_EMAIL_EMPTY = (
        By.XPATH,
        "//p[normalize-space()='Please enter an email address or phone number.']"
    )

    ERROR_MESSAGE_EMAIL_INVALID = (
        By.XPATH,
        "//p[normalize-space()='Please enter a valid email address.']"
    )

    ERROR_MESSAGE_PASS_EMPTY = (
        By.XPATH,
        "//p[normalize-space()='Please enter a password.']"
    )

    ERROR_MESSAGE_INVALID_CREDENTIAL = (
        By.XPATH,
        "//p[normalize-space()='Wrong email or password.']"
    )

    ERROR_MESSAGE_WRONG_PASSWORD = (
        By.XPATH,
        "//p[normalize-space()='Wrong email or password.']"
    )

    ERROR_MESSAGE_EMAIL_PASS_EMPTY = (
        By.XPATH,
        "//p[normalize-space()='Please enter an email address or phone number.']"
    )

    SUCCESS_MESSAGE = (
        By.ID,
        "«r2»"
    )

    # -----------------------------
    # Methods
    # -----------------------------

    def enter_email(self, email):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EMAIL
            )
        )
        element.click()
        element.send_keys(email)

    # -----------------------------

    def enter_password(self, password):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.PASSWORD
            )
        )

        element.click()
        element.send_keys(password)

    # -----------------------------

    def click_login(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.LOGIN_BUTTON
            )
        )[1].click()

    # -----------------------------

    def get_error_message_email_empty(self):

        elements =  self.wait.until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGE_EMAIL_EMPTY
            )
        )
        for element in elements:
            if element.is_displayed():
                return element.text
            
        raise Exception ("Visible error message not found")
    
    # -----------------------------

    def get_error_message_email_pass_empty(self):

        elements =  self.wait.until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGE_EMAIL_PASS_EMPTY
            )
        )
        for element in elements:
            if element.is_displayed():
                return element.text
            
        raise Exception ("Visible error message not found")
    
    def get_error_message_email_invalid(self):

        elements =  self.wait.until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGE_EMAIL_INVALID
            )
        )
        for element in elements:
            if element.is_displayed():
                return element.text
            
        raise Exception ("Visible error message not found")
    
    def get_error_message_invalid_credential(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGE_INVALID_CREDENTIAL
            )
        )
        for element in elements:
            if element.is_displayed():
                return element.text
                
        raise Exception ("Visible error message not found")
    
    def get_error_message_pass_empty(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGE_PASS_EMPTY
            )
        )
        for element in elements:
            if element.is_displayed():
                return element.text
            
        raise Exception ("Visible error message not found")

    # -----------------------------

    def get_success_message(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.SUCCESS_MESSAGE
            )
        )
        if elements.is_displayed():
            return "Logged in"
            
        raise Exception ("Visible error message not found")

    # -----------------------------

    # def clear_email(self):

    #     self.driver.find_element(
    #         *self.EMAIL
    #     ).clear()

    # # -----------------------------

    # def clear_password(self):

    #     self.driver.find_element(
    #         *self.PASSWORD
    #     ).clear()

    # -----------------------------

    # def click_show_password(self):

    #     self.wait.until(
    #         EC.element_to_be_clickable(
    #             self.SHOW_PASSWORD
    #         )
    #     ).click()

    # -----------------------------

    def is_password_hidden(self):

        field = self.driver.find_element(
            *self.PASSWORD
        )

        return field.get_attribute("type") == "password"

    # -----------------------------

    # def get_email_field(self):

    #     return self.driver.find_element(
    #         *self.EMAIL
    #     )

    # # -----------------------------

    # def get_password_field(self):

    #     return self.driver.find_element(
    #         *self.PASSWORD
    #     )

    # -----------------------------

    def login(self, email, password):

        self.enter_email(email)

        self.enter_password(password)

        self.click_login()