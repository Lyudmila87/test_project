from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    INPUT_LOGIN_EMAIL=(By.CSS_SELECTOR, '#id_login-username' )
    LOGIN_FORM=(By.CSS_SELECTOR,'#login_form')
    INPUT_LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    BUTTON_LOGIN=(By.CSS_SELECTOR, '#login_form > button')

    INPUT_REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    INPUT_REPEAT_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET=(By.CSS_SELECTOR,'.btn-add-to-basket')
    PRODUCT_NAME=(By.CSS_SELECTOR,'.product_main > h1')
    ADDED_PRODUCT_NAME=(By.XPATH,"//div[contains(@class, 'alert')][1]/div[@class='alertinner ']/strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,'.product_main > .price_color')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')