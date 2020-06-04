from pages.base_page import BasePage
from locators.header_locator import HeaderLocator
from locators.general_locator import GeneralLocator


class HeaderPage(BasePage, HeaderLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def text_digit_cart_header(self):
        return self.get_web_element(self.digit_cart_header).text

    def text_cart_header_price(self):
        return self.get_web_element(self.cart_header_price).text

    def check_text_digit_cart_header(self, digit):
        return self.text_present_in_element(self.digit_cart_header, digit)

    def text_h1(self):
        return self.get_web_element(self.h1).text
