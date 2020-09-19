from helpers.locators import Locators

class MixinSEO:
    def __init__(self):
        self.locators = Locators()
        self.breadcrumbs_last_el = self.locators.breadcrumbs_current_path
        self.breadcrumbs_devider = self.locators.breadcrumbs_devider
        self.tag_h1 = self.locators.h1
        self.cars_block_title = self.locators.car_descendants_wrapper_h2
        self.breadcrumbs = self.locators.breadcrumbs
        self.popular_manufactures = self.locators.popular_manufactures
        self.cars_block = self.locators.car_descendants_wrapper_a

