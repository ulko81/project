from helpers.locators import Locators
from helpers.methods import Methods


class MixinCart:
    def __init__(self):
        self.locators = Locators()
        self.methods = Methods()
        self.button_blue = self.locators.btn_blue
        self.button_green = self.locators.btn_green
        self.cart_remove_item_button = self.locators.cart_remove
        self.button_plus = self.locators.button_increment
        self.button_minus = self.locators.button_decrement
        self.price = self.locators.grid_table_price
        self.price_total = self.locators.total_wrapper_price_total
        self.recommended_price = self.locators.info_block_price
        self.recommended_name = self.locators.info_block_name
        self.recommended_brand = self.locators.info_block_brand
        self.recommended_vendor_code = self.locators.info_block_vendor_code
        self.recommended_delivery = self.locators.info_block_delivery
        self.name = self.locators.grid_table_name
        self.brand = self.locators.grid_table_brand
        self.vendor_code = self.locators.grid_table_vendor_code
        self.delivery_date = self.locators.grid_table_delivery_date
        self.price_sum = self.locators.grid_table_price_sum
        self.field_count = self.locators.quantity_field
        self.get_vendor_code = self.methods.get_vendor_code
        self.change_format_date = self.methods.change_format_date_cart
