from helpers.locators import Locators


class MixinSearch:
    def __init__(self):
        self.locators = Locators()
        self.recommended_vendor_code = self.locators.name_inner_vendor_code
        self.recommended_name = self.locators.name_inner_name
        self.recommended_brand = self.locators.name_inner_brand
        self.recommended_price = self.locators.price_wrapper_price
        self.recommended_delivery = self.locators.general_info_delivery
        self.recommended_button_blue = self.locators.price_wrapper_button_blue
        self.recommended_button_green = self.locators.price_wrapper_button_green
        self.first_offer_button_blue = self.locators.nested_row_0_button_blue
        self.first_offer_button_green = self.locators.nested_row_0_button_green
        self.first_offer_price = self.locators.nested_row_0_price
        self.first_offer_vendor_code = self.locators.nested_row_0_vendor_code
        self.first_offer_name = self.locators.nested_row_0_name
        self.first_offer_brand = self.locators.nested_row_0_brand
        self.first_offer_delivery = self.locators.nested_row_0_delivery