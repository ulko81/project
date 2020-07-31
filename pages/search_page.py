from pages.base_page import BasePage
from locators.search_locator import SearchLocator


class SearchPage(BasePage, SearchLocator):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def list_search_recommended_prices(self):
        vendor_codes = self.get_web_elements(self.search_recommended_vendor_code)
        prices = self.get_web_elements(self.search_recommended_price)
        vendor_codes_with_prices = set(zip(map(lambda el: el.text, vendor_codes), map(lambda el: el.text, prices)))
        return list(map(lambda el: el[1], vendor_codes_with_prices))

    @property
    def get_search_recommended_buttons_buy(self):
        return self.get_web_elements(self.search_recommended_button_blue)

    @property
    def get_search_recommended_buttons_in_cart(self):
        return self.get_web_elements(self.search_recommended_button_green)

    @property
    def amount_of_search_recommended_buttons_in_cart(self):
        return self.amount_of_elements(self.search_recommended_button_green)

    @property
    def get_first_offers_buy_button(self):
        return self.get_web_elements(self.search_first_offer_button_blue)

    @property
    def get_first_offers_in_cart_button(self):
        return self.get_web_elements(self.search_first_offer_button_green)

    @property
    def amount_first_offers_button_in_cart(self):
        return self.amount_of_elements(self.search_first_offer_button_green)

    @property
    def list_text_first_search_block_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.search_first_offer_price)))

    def text_recomended_name(self, order):
        return self.get_web_elements(self.search_recommended_name)[order].text

    def text_offer_name(self, order):
        return self.get_web_elements(self.search_first_offer_name)[order].text

    def text_recomended_brand(self, order):
        return self.get_web_elements(self.search_recommended_brand)[order].text

    def text_offer_brand(self, order):
        return self.get_web_elements(self.search_first_offer_brand)[order].text

    def text_recomended_vendor_code(self, order):
        return self.get_web_elements(self.search_recommended_vendor_code)[order].text

    def text_offer_vendor_code(self, order):
        return self.get_web_elements(self.search_first_offer_vendor_code)[order].text

    def text_recomended_delivery(self, order):
        return self.get_web_elements(self.search_recommended_delivery)[order].text.lower()

    def text_offer_delivery(self, order):
        return self.get_web_elements(self.search_first_offer_delivery)[order].text.lower()

    def text_recomended_price(self, order):
        return self.get_web_elements(self.search_recommended_price)[order].text

    def text_offer_price(self, order):
        return self.get_web_elements(self.search_first_offer_price)[order].text

    def set_recomended_product_info(self, order):
        return {self.text_recomended_name(order), self.text_recomended_brand(order),
                self.text_recomended_vendor_code(order), self.text_recomended_delivery(order),
                self.text_recomended_price(order)}

    def set_offer_product_info(self, order):
        return {self.text_offer_name(order), self.text_offer_brand(order), self.text_offer_vendor_code(order),
                self.text_offer_delivery(order), self.text_offer_price(order)}
