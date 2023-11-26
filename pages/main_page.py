from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """класс для работы с элементами главной страницы"""
    def __init__(self,*args,**kwargs):
        """функция-заглушка"""
        super(MainPage,self).__init__(*args,**kwargs)