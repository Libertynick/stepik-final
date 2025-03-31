from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_none_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAVE_NOT_ANY), \
            "В корзине уже что то добавлено"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_EMPTY), "Нет сообщения о том, что корзина пуста"