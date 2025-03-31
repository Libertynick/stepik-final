from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def should_be_login_page(self, email, password):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user(email,password)

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url.lower(), "Нет такого вхождения слова в юрл"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form dont find"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form dont find"
        assert True

    def register_new_user(self, email, password):
        email_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.REGISTER_EMAIL_ADDRESS))
        email_input.send_keys(email)

        password_input_1 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.REGISTER_PASSWORD_ADDRESS_1))
        password_input_1.send_keys(password)

        password_input_2 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.REGISTER_PASSWORD_ADDRESS_2))
        password_input_2.send_keys(password)

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.BUTTON_REGISTER)).click()
        assert True