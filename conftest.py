from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """обработка аргументов командной строки"""
    parser.addoption('--language', action='store', default="en")
    parser.addoption('--browser_name', action='store', default='chrome')


@pytest.fixture(scope="function")
def browser(request):
    """фикстура для создания и закрытия экземпляра браузера"""
    language = request.config.getoption("language")
    browser_name=request.config.getoption('browser_name')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



