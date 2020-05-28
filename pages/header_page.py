from pages.base_page import BasePage
from locators.header_locator import HeaderLocator


class HeaderPage(BasePage, HeaderLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def text_digit_cart_header(self):
        return self.get_web_element(self.digit_cart_header).text

    def text_cart_header_price(self):
        return self.get_web_element(self.cart_header_price).text