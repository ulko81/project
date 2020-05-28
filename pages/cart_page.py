from pages.base_page import BasePage
from locators.cart_locator import CartLocator


class CartPage(BasePage, CartLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def text_count_in_icon_cart(self, driver):
        return self.get_web_element(driver, self.cart_count).text

