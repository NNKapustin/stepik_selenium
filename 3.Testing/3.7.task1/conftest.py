import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()
