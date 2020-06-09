from pages.base_page import BasePage
from locators.header_locator import HeaderLocator
from locators.general_locator import GeneralLocator


class HeaderPage(BasePage, HeaderLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def text_digit_cart_header(self):
        return self.get_web_element(self.digit_cart_header).text

    def text_cart_price(self):
        return self.get_web_element(self.cart_header_price).text

    def check_text_digit_cart_header(self, digit):
        return self.text_present_in_element(self.digit_cart_header, digit)

    def click_empty_profile(self):
        self.click(self.profile_empty)

    def fill_module_phone_field(self, phone):
        self.get_web_element(self.phone_field).send_keys(phone)

    def fill_module_pass_field(self, password):
        self.get_web_element(self.pass_field).send_keys(password)

    def click_module_enter(self):
        self.click(self.button_blue)

    def click_cart_in_header(self):
        self.click(self.cart_with_items)
