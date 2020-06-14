from pages.base_page import BasePage
from methods.general_func import change_format_date_cart
from locators.text_field import TextField, CartTextField
from locators.button import CartButton, Button


class CartPage(BasePage, TextField, CartTextField, CartButton, Button):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button_recomended(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_present_button_in_cart_recomended(self):
        return self.get_web_element(self.button_green)

    @property
    def text_price(self):
        return self.get_web_element(self.cart_product_price).text.replace('.0', '')

    def text_first_price_recomended(self):
        return self.get_web_elements(self.cart_recommended_price)[0].text.lower()

    @property
    def text_name(self):
        return self.get_web_element(self.cart_product_name).text

    @property
    def text_brand(self):
        return self.get_web_element(self.cart_product_brand).text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.cart_product_vendor_code).text

    @property
    def text_delivery(self):
        return change_format_date_cart(self.get_web_element(self.cart_product_delivery_date).text).lower()

    def set_product_info(self):
        return {self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery, self.text_price}




