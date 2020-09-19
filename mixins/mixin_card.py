from helpers.locators import Locators


class MixinCard:
    def __init__(self):
        self.locators = Locators()
        self.button_blue = self.locators.list_item_button_blue
        self.button_green = self.locators.list_item_button_green
        self.first_offer_button_blue = self.locators.grid_table_first_offer_button_blue
        self.first_offer_button_green = self.locators.grid_table_first_offer_button_green
        self.price = self.locators.product_short_info_price
        self.first_offer_price = self.locators.grid_table_first_offer_price
        self.first_offer_name = self.locators.grid_table_first_offer_name
        self.first_offer_brand = self.locators.grid_table_first_offer_brand
        self.tag_h1 = self.locators.h1
        self.brand = self.locators.short_info_block_brand
        self.vendor_code = self.locators.short_info_block_vendor_code
        self.delivery = self.locators.product_short_info_delivery
        self.first_offer_delivery = self.locators.grid_table_first_offer_delivery
        self.first_offers = self.locators.grid_table_first_offers
        self.first_offer_vendor_code = self.locators.grid_table_first_offer_vendor_code
        self.product_attributes_values = self.locators.product_attributes_values
