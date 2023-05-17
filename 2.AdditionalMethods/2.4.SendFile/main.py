from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys('Nick')
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('Smith')
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys('smith@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем директорию исполняемого файла
    file_name = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, "input[name='file']").send_keys(file_name)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)
