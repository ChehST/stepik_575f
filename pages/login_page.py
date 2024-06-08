import time

from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url , "url doesn't match"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def register_new_user(self, email, password):
        self.find(*LoginPageLocators.REGISTRATIOM_MAIL_INPUT).send_keys(email)
        self.find(*LoginPageLocators.REGISTRATIOM_PASSWORD_INPUT).send_keys(password)
        self.find(*LoginPageLocators.REGISTRATIOM_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find(*LoginPageLocators.REG_BTN).click()
        self.should_be_authorized_user()

    