from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):
    def check_basket_empty(self):
        assert self.is_element_present(*BasketLocators.BASKET_IS_EMPTY), "Должно быть сообщение, что корзина пуста"

    def check_empty_basket(self):
        assert not self.is_element_present(*BasketLocators.ITEMS_TO_BUY), "Корзина должна быть пустой"