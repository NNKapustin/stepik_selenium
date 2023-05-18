import time

from selenium.webdriver.common.by import By


def test_add_to_basket_lang(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert add_to_cart_button.text, 'There is no text on button'
