from pages.base_page import BasePage
from methods.general_method import GeneralMethod
from locators.cart_locator import CartLocator


class CartPage(BasePage, CartLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button_recommended(self):
        self.get_web_elements(self.button_blue)[0].click()

    @property
    def check_present_button_in_cart_recommended(self):
        return self.get_web_element(self.button_green)

    @property
    def text_price(self):
        return self.get_web_element(self.cart_price).text.replace('.0', '')

    @property
    def text_first_recommended_price(self):
        return self.get_web_elements(self.cart_recommended_price)[0].text.lower()

    @property
    def text_name(self):
        return self.get_web_element(self.cart_name).text

    @property
    def text_first_recommended_name(self):
        return self.get_web_elements(self.cart_recommended_name)[0].get_attribute('title')

    @property
    def text_brand(self):
        return self.get_web_element(self.cart_brand).text

    @property
    def text_first_recommended_brand(self):
        return self.get_web_elements(self.cart_recommended_brand)[0].text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.cart_vendor_code).text

    @property
    def text_first_recommended_vendor_code(self):
        return GeneralMethod.get_vendor_code(self.get_web_elements(self.cart_recommended_brand)[0].text,
                               self.get_web_elements(self.cart_recommended_vendor_code)[0].text)

    @property
    def text_delivery(self):
        return GeneralMethod.change_format_date_cart(self.get_web_element(self.cart_delivery_date).text).lower()

    @property
    def text_first_recommended_delivery(self):
        return self.get_web_elements(self.cart_recommended_delivery)[0].text.lower()

    def set_product_info(self):
        return {self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery, self.text_price}

    def set_recommended_product_info(self):
        return {self.text_first_recommended_name, self.text_first_recommended_brand,
                self.text_first_recommended_vendor_code, self.text_first_recommended_delivery,
                self.text_first_recommended_price}
