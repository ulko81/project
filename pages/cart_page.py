from pages.base_page import BasePage
from locators.cart_locator import CartLocator
from locators.general_locator import GeneralLocator
from methods.general_func import change_format_date_cart


class CartPage(BasePage, CartLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button_recomended(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_present_button_in_cart_recomended(self):
        return self.get_web_element(self.button_green)

    def text_price(self):
        return self.get_web_elements(self.price)[0].text.replace('.0', '')

    def text_name(self):
        print(self.get_web_element(self.product_name).text)
        return self.get_web_element(self.product_name).text

    def text_brand(self):
        print(self.get_web_element(self.product_brand).text)
        return self.get_web_element(self.product_brand).text

    def text_vendor_code(self):
        print(self.get_web_element(self.product_vendor_code).text)
        return self.get_web_element(self.product_vendor_code).text

    def text_delivery(self):
        print(change_format_date_cart(self.get_web_element(self.product_delivery).text))

        return change_format_date_cart(self.get_web_element(self.product_delivery).text)

    def set_product_info(self):
        return {self.text_name(), self.text_brand(), self.text_vendor_code(), self.text_delivery()}




