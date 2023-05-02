from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
    input3.send_keys("test@test.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.first_class input').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.second_class input').send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.third_class input').send_keys("Smolensk")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
