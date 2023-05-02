from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/math.html")

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

