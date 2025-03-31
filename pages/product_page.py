from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        product_link.click()

    def proverka_name_coast(self):
        name_book = self.get_name_book()
        price_book = self.get_price_book()
        self.proverka_name(name_book)
        self.proverka_coast(price_book)

    def get_name_book(self):
        name_book = WebDriverWait(self.browser, 10).until(
        EC.visibility_of_element_located(ProductPageLocators.NAME_BOOK))
        return name_book.text

    def get_price_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        return price_book

    def proverka_name(self, name_book):
        assert name_book == self.browser.find_element(*ProductPageLocators.NAME_BOOK_MESSAGE).text, 'Не совпадает добавленная книга с выбранной книгой'

    def proverka_coast(self, price_book):
        assert price_book == self.browser.find_element(*ProductPageLocators.PRICE_BOOK_MESSAGE).text, 'Не совпадает цена добавленной книги с ценой выбранной книги'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"