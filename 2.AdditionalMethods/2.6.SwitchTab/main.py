from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    new_window = browser.window_handles[1] # window_handles object which contains all tabs
    # previous_window = browser.window_handles[0] # if we need to return
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    y = log(abs(12 * sin(x)))
    browser.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)
