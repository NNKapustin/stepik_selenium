import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

# execute_script выполняет javascript код, заключенный в кавычки
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
y = log(abs(12*sin(x)))

browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
rb = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", rb) # скролл чтобы элемент был виден
rb.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скролл чтобы элемент был виден
button.click()

time.sleep(10)
