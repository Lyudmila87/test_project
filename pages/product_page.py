from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_basket(self):
        """метод для добавления в корзину"""
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BUTTON_ADD_TO_BASKET)
        )
        button.click()

    def check_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME).text, 'название товара не соответствует'

    def check_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_PRICE).text, 'цена товара не соответствует'
