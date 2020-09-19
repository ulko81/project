from helpers.locators import Locators


class MixinCheckout:
    def __init__(self):
        self.locators = Locators()
        self.button_blue = self.locators.btn_blue
        self.multi_user_block = self.locators.user_change_counterparty_button
        self.username = self.locators.user_title_username
        self.delivery_tooltip = self.locators.preloader
        self.phone_field = self.locators.phone_field
        self.password_field = self.locators.password_field
