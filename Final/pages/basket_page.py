from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_empty_basket(self):
        #проверяем, что на странице есть элемент, который выводит сообщение о том, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_LINK), "Bascket is not empty"

        #проверяем, что на странице BasketPage нет кнопки "Перейти к оформлению"
        assert self.is_not_element_present(*BasketPageLocators.BUTTON_PROTECTED_TO_CHECKOUT_LINK)



