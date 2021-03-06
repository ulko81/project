from pages.base_page import BasePage
from mixins.mixin_main import MixinMain
from helpers.functions import get_vendor_code


class MainPage(BasePage, MixinMain):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinMain.__init__(self)

    def click_first_buy_button_you_watched(self):
        self.get_web_elements(self.you_watched_button_blue)[0].click()

    def click_first_in_cart_button_you_watched(self):
        self.get_web_elements(self.you_watched_button_green)[0].click()

    @property
    def check_button_in_cart_you_watched(self):
        return self.get_web_element(self.you_watched_button_green)

    @property
    def text_first_price(self):
        return self.get_web_elements(self.price)[0].text.lower()

    @property
    def text_first_name(self):
        return self.get_web_elements(self.name)[0].text

    @property
    def text_first_brand(self):
        return self.get_web_elements(self.brand)[0].text

    @property
    def text_first_vendor_code(self):
        return get_vendor_code(self.get_web_elements(self.brand)[0].text, self.get_web_elements
        (self.vendor_code)[0].text)

    @property
    def text_first_delivery(self):
        return self.get_web_elements(self.delivery)[0].text.lower()

    def set_you_watched_product_info(self):
        return {self.text_first_name, self.text_first_brand, self.text_first_vendor_code, self.text_first_delivery,
                self.text_first_price}

    @property
    def text_title_block(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.title_block)))

    @property
    def tuple_popular_manufactures(self):
        return tuple(map(lambda el: el.get_attribute('href'), self.get_web_elements(self.popular_manufactures)))

    @property
    def tuple_popular_models(self):
        return tuple(map(lambda el: el.get_attribute('href'), self.get_web_elements(self.popular_models)))

    @property
    def tuple_popular_categories(self):
        return tuple(map(lambda el: el.get_attribute('href'), self.get_web_elements(self.popular_categories)))

    @property
    def text_seo_after_autogid(self):
        return self.get_web_element(self.seo_text).text

    @property
    def get_guide_tabs(self):
        return self.get_web_elements(self.guide_tabs)

    @property
    def text_guide_tab_selected(self):
        return self.get_web_element(self.guide_tab_selected).text

    def click_search_field(self):
        self.click(self.search_field)

    def fill_search_field(self, query):
        self.get_web_element(self.input_search_field).send_keys(query)

    def click_search_button(self):
        self.click(self.icon_search)

    def check_search_full_result(self):
        return self.get_web_element(self.full_search_result)
