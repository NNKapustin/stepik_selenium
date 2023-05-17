import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():  # можно маркировать целый тестовый класс - маркировка будет применена ко всем тестовым методам, входящим в класс.
    # @pytest.mark.skip - метка для тестов, которые нужно пропустить
    # @pytest.mark.xfail(reason='bug fixing') - метка тестов, которые ожидаемо упадут, например на время исправления, причину можно указать в параметре reason
    # pytest -v test_main.py - запуск
    # pytest -rx -v test_main.py - для отображения reason
    # pytest -rX -v test_main.py - для отображения подробной информации
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link_on_win10(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# pytest -s -v -m smoke test_main.py - запуск тестов с определенной меткой
# pytest -s -v -m "not smoke" test_main.py - запуск всех кроме указанной метки
# pytest -s -v -m "smoke or regression" test_main.py - запуск с тестов с указанными метками
# pytest -s -v -m "smoke and win10" test_main.py - запуск тестов со всеми указанными метками
# pytest.ini - описание наборов тестов, без него будет warning при выполнении
