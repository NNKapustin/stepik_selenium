from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):

        with webdriver.Chrome() as browser:
            browser.implicitly_wait(5)
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
            input3.send_keys("test@test.ru")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration error')

    def test_registration_2(self):
        with webdriver.Chrome() as browser:
            browser.implicitly_wait(5)
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
            input3.send_keys("test@test.ru")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration error')


if __name__ == "__main__":
    unittest.main()
