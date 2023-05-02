import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# execute_script выполняет javascript код, заключенный в кавычки
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# browser.execute_script("window.scrollBy(0, 100);") # скролл на 100 px вниз
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скролл чтобы элемент был виден
button.click()


time.sleep(10)
