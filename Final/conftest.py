from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
