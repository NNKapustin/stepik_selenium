from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def click_add_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
