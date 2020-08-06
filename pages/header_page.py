from pages.base_page import BasePage
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

    def click_cart(self):
        self.click(self.cart_with_items)

    def click_module_language_option(self, text):
        self.get_element_with_text(text).click()

    def click_language_select(self):
        self.click(self.header_language_select)

    @property
    def text_current_language(self):
        return self.get_web_element(self.header_language_select).text

    @property
    def text_profile_user(self):
        return self.get_web_element(self.profile_with_auth).text

    def text_mega_menu(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.mega_menu)))

    def text_user_menu(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.user_menu)))

    def text_contact(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.contact)))

    def get_first_multi_users(self):
        return self.get_first_visible_element(self.multi_user_block)

    def click_my_car(self):
        self.click(self.my_car_empty)

    @property
    def check_empty_my_car(self):
        return self.get_web_element(self.my_car_empty)

    @property
    def text_my_car(self):
        return self.get_web_element(self.my_car_with_car).text
