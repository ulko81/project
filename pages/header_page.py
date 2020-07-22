from pages.base_page import BasePage
from methods.cart_method import CartMethod
from locators.header_locator import HeaderLocator


class HeaderPage(BasePage, HeaderLocator):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def text_digit_cart_header(self):
        return self.get_web_element(self.cart_header_digit).text

    @property
    def text_cart_price(self):
        return self.get_web_element(self.cart_header_price).text.lower()

    def check_text_digit_cart_header(self, digit):
        return self.text_present_in_element(self.cart_header_digit, digit)

    def check_profile_auth(self):
        return self.get_web_element(self.profile_with_auth)

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

    @property
    def text_price(self):
        return self.get_web_element(self.module_product_price).text

    def check_cart_module_info_loaded(self, text):
        return self.text_present_in_element(self.module_product_price, text)

    @property
    def text_name(self):
        return self.get_web_element(self.module_product_name).text

    @property
    def text_brand(self):
        return self.get_web_element(self.module_product_brand).text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.module_product_vendor_code).text

    @property
    def text_delivery(self):
        return CartMethod.change_format_date_cart(self.get_web_element(self.module_product_delivery).text).lower()

    def set_product_info(self):
        return {self.text_price, self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery}

    def click_module_language_option(self, text):
        self.get_element_with_text(text).click()

    def click_language_select(self):
        self.click(self.header_language_select)

    @property
    def text_current_language(self):
        return self.get_web_element(self.header_language_select).text

    @property
    def text_languages_module(self):
        return ' '.join(tuple(map(lambda el: el.text, self.get_web_elements(self.module_language_select))))

    @property
    def text_profile_user(self):
        return self.get_web_element(self.profile_with_auth).text

    def click_module_button_order(self):
        self.click(self.module_button_cart_order)

    def text_mega_menu(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.mega_menu)))

    def text_user_menu(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.user_menu)))

    def text_contact(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.contact)))
