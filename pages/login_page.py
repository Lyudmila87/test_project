from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self._browser.current_url, "'login' нет в текущем url браузера"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не существует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Форма регистрации не существует"

    def register_new_user(self, email, password):
        self._browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self._browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self._browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_SUBMIT).send_keys(password)
        self._browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def open_login_page(self):
        self._browser.get(self.url+"ru/accounts/login/")
