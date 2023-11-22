from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """общие методы для работы с браузером"""

    def __init__(self, browser: WebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """открываем ссылку"""
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        """метод для перехвата исключений.
        Два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор)"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
