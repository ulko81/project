from pages.base_page import BasePage
from mixins.mixin_checkout import MixinCheckout


class CheckoutPage(BasePage, MixinCheckout):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinCheckout.__init__(self)

    def fill_checkout_phone_field(self, phone):
        self.get_web_element(self.phone_field).send_keys(phone)

    def fill_checkout_pass_field(self, password):
        self.get_web_element(self.password_field).send_keys(password)

    def click_checkout_enter(self):
        self.click(self.button_blue)

    @property
    def text_checkout_user_name(self):
        return self.get_web_element(self.username).text

    def check_load_checkout(self):
        self.get_web_element(self.delivery_tooltip)

    def get_first_multi_users(self):
        return self.get_first_visible_element(self.multi_user_block)
