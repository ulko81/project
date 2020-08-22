from pages.base_page import BasePage
from methods.general_method import GeneralMethod
from locators.full_search_product_locator import FullSearchProductLocator


class FullSearchProductPage(BasePage, FullSearchProductLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button(self):
        self.get_web_elements(self.button_blue)[0].click()

    def click_first_in_cart_button(self):
        self.get_web_elements(self.button_green)[0].click()

    @property
    def check_button_in_cart(self):
        return self.get_web_elements(self.button_green)[0]

    @property
    def text_first_price(self):
        return GeneralMethod.change_format_price(self.get_web_element(self.base_price).text.lower())

    @property
    def text_first_name(self):
        return self.get_web_elements(self.base_name)[0].text

    @property
    def text_first_brand(self):
        return self.get_web_elements(self.base_brand)[0].text

    @property
    def text_first_vendor_code(self):
        return GeneralMethod.get_vendor_code(self.get_web_elements(self.base_brand)[0].text,
                                             self.get_web_elements(self.base_vendor_code)[0].text)

    @property
    def text_first_delivery(self):
        return self.get_web_elements(self.base_delivery)[0].text.lower()

    def set_product_info(self):
        return {self.text_first_name, self.text_first_brand, self.text_first_vendor_code, self.text_first_delivery,
                self.text_first_price}
