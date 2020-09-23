from helpers.locators import Locators


class MixinCatalog:

    def __init__(self):
        self.locators = Locators()
        self.button_blue = self.locators.btn_blue
        self.button_green = self.locators.btn_green
        self.price = self.locators.catalogue_list_price
        self.name = self.locators.catalogue_list_name
        self.brand = self.locators.catalogue_list_brand
        self.delivery = self.locators.catalogue_list_delivery
        self.vendor_code = self.locators.catalogue_list_vendor_code
        self.seo_our_cities = self.locators.container_our_cities
        self.cars_block_title = self.locators.car_descendants_wrapper_h2
        self.input_search_field = self.locators.search_input
        self.category_in_search_result = self.locators.search_results_a
