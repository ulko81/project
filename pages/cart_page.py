from pages.base_page import BasePage
from mixins.mixin_cart import MixinCart


class CartPage(BasePage, MixinCart):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinCart.__init__(self)

    def click_first_buy_button_recommended(self):
        self.get_web_elements(self.button_blue)[0].click()

    @property
    def check_present_button_in_cart_recommended(self):
        return self.get_web_element(self.button_green)

    @property
    def text_price(self):
        return self.get_web_element(self.price).text.replace('.0', '')

    @property
    def text_price_total(self):
        return self.get_web_element(self.price_total).text.replace('.0', '')

    @property
    def text_first_recommended_price(self):
        return self.get_web_elements(self.recommended_price)[0].text.lower()

    @property
    def text_name(self):
        return self.get_web_element(self.name).text

    @property
    def text_first_recommended_name(self):
        return self.get_web_elements(self.recommended_name)[0].get_attribute('title')

    @property
    def text_brand(self):
        return self.get_web_element(self.brand).text

    @property
    def text_first_recommended_brand(self):
        return self.get_web_elements(self.recommended_brand)[0].text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.vendor_code).text

    @property
    def text_first_recommended_vendor_code(self):
        return self.get_vendor_code(self.get_web_elements(self.recommended_brand)[0].text,
                                             self.get_web_elements(self.recommended_vendor_code)[0].text)

    @property
    def text_delivery(self):
        return self.change_format_date(self.get_web_element(self.delivery_date).text).lower()

    @property
    def text_first_recommended_delivery(self):
        return self.get_web_elements(self.recommended_delivery)[0].text.lower()

    def set_product_info(self):
        return {self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery, self.text_price}

    def set_recommended_product_info(self):
        return {self.text_first_recommended_name, self.text_first_recommended_brand,
                self.text_first_recommended_vendor_code, self.text_first_recommended_delivery,
                self.text_first_recommended_price}

    def click_button_remove_item(self):
        self.click(self.cart_remove_item_button)

    def click_button_plus(self):
        self.click(self.button_plus)

    def click_button_minus(self):
        self.click(self.button_minus)

    def check_field_digit_field_count(self, digit):
        return self.value_present_in_element(self.field_count, digit)

    def check_sum_price(self, price):
        return self.text_present_in_element(self.price_sum, price)

    def check_total_price(self, price):
        return self.text_present_in_element(self.price_total, price)
