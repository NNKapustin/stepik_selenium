from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # alert window can only be accepted
    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # alert.accept()

    # confirm window can be accepted or dismissed
    confirm = browser.switch_to.alert
    # confirm_text = confirm.text
    confirm.accept()
    # confirm.dismiss()

    # prompt window can be filled by text, accepted and dismissed
    # prompt = browser.switch_to.alert
    # prompt_text = prompt.text
    # prompt.send_keys("My answer")
    # prompt.accept()
    # prompt.dismiss()

    time.sleep(1)
    x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    y = log(abs(12*sin(x)))
    browser.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)
