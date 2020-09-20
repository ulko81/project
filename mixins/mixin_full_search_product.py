from helpers.locators import Locators


class MixinFullSearchProduct:
    def __init__(self):
        self.locators = Locators()
        self.button_blue = self.locators.btn_blue
        self.button_green = self.locators.btn_green
        self.price = self.locators.catalogue_list_price
        self.name = self.locators.catalogue_list_name
        self.brand = self.locators.catalogue_list_brand
        self.delivery = self.locators.catalogue_list_delivery
        self.vendor_code = self.locators.catalogue_list_vendor_code
