from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'alert')][1]/div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner ')

    def add_product_to_basket(self):
        """метод для добавления в корзину"""
        button = WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable(*self.BUTTON_ADD_TO_BASKET)
        )
        button.click()

    def check_product_name(self):
        assert self._browser.find_element(*self.PRODUCT_NAME).text == self._browser.find_element(
            *self.ADDED_PRODUCT_NAME).text, 'название товара не соответствует'

    def check_product_price(self):
        assert self._browser.find_element(*self.PRODUCT_PRICE).text == self._browser.find_element(
            *self.ADDED_PRODUCT_PRICE).text, 'цена товара не соответствует'

    def should_not_be_success_message(self):
        """success-сообщения на странице быть не должно"""
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
            "Cообщение присутствует, хотя не должно быть"

    def should_be_disappear_success_message(self):
        """success-сообщение должно исчезнуть после добавления в корзину"""
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
            "Cообщение присутствует, хотя не должно быть"

    def open_product_url(self, product_name: str, num_promo: str = None):
        if num_promo is not None:
            self._browser.get(self.url+"catalogue/" + product_name + "/?promo=" + num_promo)
        else:
            self._browser.get(self.url+"catalogue/" + product_name)

