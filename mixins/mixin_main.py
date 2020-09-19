from helpers.locators import Locators


class MixinMain:
    def __init__(self):
        self.locators = Locators()
        self.you_watched_button_blue = self.locators.info_block_button_blue
        self.you_watched_button_green = self.locators.info_block_button_green
        self.price = self.locators.info_block_wrapper_price
        self.name = self.locators.info_block_wrapper_name
        self.brand = self.locators.info_block_wrapper_brand
        self.vendor_code = self.locators.info_block_wrapper_vendor_code
        self.delivery = self.locators.info_block_wrapper_delivery
        self.title_block = self.locators.title_block
        self.seo_text = self.locators.seo_text
        self.guide_tabs = self.locators.guide_tabs
        self.guide_tab_selected = self.locators.guide_tabs
        self.popular_manufactures = self.locators.popular_manufactures
        self.popular_models = self.locators.popular_models
        self.popular_categories = self.locators.popular_categories
