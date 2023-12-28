import pytest
import time

from data.links import CODERS_BOOK_NAME
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('num_promo', ["0",
                                       "1",
                                       "2",
                                       "3",
                                       "4",
                                       "5",
                                       "6",
                                       pytest.param("7", marks=pytest.mark.xfail),
                                       "8",
                                       "9"])
def test_guest_can_add_product_to_basket(browser, num_promo):
    page = ProductPage(browser)
    page.open_product_url(CODERS_BOOK_NAME, num_promo)
    import time
    time.sleep(2.5)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open_product_url("coders-at-work_207")
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser)
    page.open_product_url("coders-at-work_207")
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open_product_url("the-city-and-the-stars_95")
    page.add_product_to_basket()
    page.should_be_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser)
    page.open_product_url("the-city-and-the-stars_95")
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open_product_url("the-city-and-the-stars_95")
    page.go_to_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open_product_url("the-city-and-the-stars_95")
    page.go_to_basket_page()
    page = BasketPage(browser)
    page.check_empty_basket()
    page.check_basket_empty()


class TestUserAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self, browser, authorize_user):
        page = ProductPage(browser)
        page.open_product_url("the-city-and-the-stars_95")
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, authorize_user):
        page = ProductPage(browser)
        page.open_product_url("the-city-and-the-stars_95")
        time.sleep(2.5)
        page.add_product_to_basket()
        page.check_product_name()
        page.check_product_price()
