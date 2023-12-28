from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(
        browser):  # команда для запуска теста: pytest -v --tb=line --language=en test_main_page.py
    page = MainPage(browser)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open_link()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser)
    page.open_link()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser)
    page.open_link()
    page.go_to_basket_page()
    page = BasketPage(browser)
    page.check_basket_empty()
