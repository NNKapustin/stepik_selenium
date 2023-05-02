from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(browser, 12)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.CSS_SELECTOR, "button#book")
    button.click()

    x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    y = log(abs(12 * sin(x)))
    browser.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()

    time.sleep(10)


