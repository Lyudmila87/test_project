from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketLocators.BASKET_IS_EMPTY), "Должно быть сообщение, что корзина пуста"

    def check_empty_basket(self):
        assert not self.is_element_present(*BasketLocators.ITEMS_TO_BUY), "Корзина должна быть пустой"