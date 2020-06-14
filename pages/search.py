from pages.base_page import BasePage
from locators.text_field import SearchTextField, TextField
from locators.button import SearchButton, Button


class SearchPage(BasePage, SearchTextField, TextField, SearchButton, Button):

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
    def amount_of_search_recommended_buttons_in_cart(self):
        return self.amount_of_elements(self.search_recommended_button_green)

    @property
    def get_first_offers_buy_button(self):
        return self.get_web_elements(self.search_first_offer_button_blue)

    @property
    def amount_first_offers_button_in_cart(self):
        return self.amount_of_elements(self.search_first_offer_button_green)

    @property
    def list_text_first_search_block_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.search_first_offer_price)))
