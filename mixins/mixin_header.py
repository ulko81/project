from helpers.locators import Locators


class MixinHeader:
    def __init__(self):
        self.locators = Locators()
        self.profile_empty = self.locators.profile_anonim
        self.profile_with_auth = self.locators.profile_avtorpol
        self.cart_with_items = self.locators.cart_with_items
        self.language_select_button = self.locators.lang_dd_button_button
        self.mega_menu = self.locators.mega_menu_link
        self.user_menu = self.locators.user_menu_toggler
        self.contact = self.locators.header_contact_nav
        self.cart_count_items = self.locators.user_menu_toggler_inner_cart_count
        self.cart_price = self.locators.cart_price
        self.multi_user_block = self.locators.user_change_counterparty_button
        self.my_car_empty = self.locators.my_car_empty
        self.my_car_with_car = self.locators.my_car_selected_car
        self.cart_without_items = self.locators.cart_without_items

