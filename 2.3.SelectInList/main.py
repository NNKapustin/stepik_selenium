from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


with webdriver.Chrome() as browser:
    browser.get(" https://suninjuly.github.io/selects1.html")

    x1 = int(browser.find_element(By.ID, 'num1').text)
    x2 = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(f'{x1 + x2}') # select_by_index, select_by_value

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)