from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    REGISTER_EMAIL_ADDRESS = (By.XPATH, "//input[@name='registration-email']")
    REGISTER_PASSWORD_ADDRESS_1 = (By.XPATH, "//input[@name='registration-password1']")
    REGISTER_PASSWORD_ADDRESS_2 = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGISTER = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators:
    PRODUCT_PAGE = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICE_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")
    NAME_BOOK_MESSAGE = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    PRICE_BOOK_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner '][contains(.,' has been added to your basket.')]")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_HAVE_NOT_ANY = (By.XPATH, "//img[@class='thumbnail']")
    BASKET_MESSAGE_EMPTY = (By.XPATH, "//p")