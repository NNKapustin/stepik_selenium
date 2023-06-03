import time

from selenium.webdriver.common.by import By


def test_add_to_basket_lang(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket'), 'Add to basket button is not found'
