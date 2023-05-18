import pytest
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'
                                  ])
def test_login(browser, link):
    load_dotenv()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login").click()
    browser.find_element(By.CSS_SELECTOR, "input#id_login_email").send_keys(os.getenv('NAME'))
    browser.find_element(By.CSS_SELECTOR, "input#id_login_password").send_keys(os.getenv('PASS'))
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    WebDriverWait(browser, 5).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.box")))
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert result == 'Correct!', 'Answer is not correct!'

