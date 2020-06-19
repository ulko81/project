from pages.base_page import BasePage
from locators.text_field import TextField, CheckoutTextField
from locators.input_field import InputField
from locators.button import Button


class CheckoutPage(BasePage, InputField, Button, TextField, CheckoutTextField):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_checkout_phone_field(self, phone):
        self.get_web_element(self.phone_field).send_keys(phone)

    def fill_checkout_pass_field(self, password):
        self.get_web_element(self.pass_field).send_keys(password)

    def click_checkout_enter(self):
        self.click(self.button_blue)

    @property
    def text_checkout_user_name(self):
        return self.get_web_element(self.checkout_user_name).text

    def check_load_checkout(self):
        self.get_web_element(self.delivery_tooltip)
