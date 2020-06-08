from pages.base_page import BasePage
from locators.search_locator import SearchLocator
from locators.general_locator import GeneralLocator


class SearchPage(BasePage, SearchLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def set_tuple_search_recommended_articules_with_price(self):
        vendor_codes = self.get_web_elements(self.search_recommended_vendor_codes)
        prices = self.get_web_elements(self.search_recommended_prices)
        articule_with_price = set(zip(map(lambda el: el.text, vendor_codes), map(lambda el: el.text, prices)))
        return list(map(lambda el: el[1], articule_with_price))

    def get_search_recommended_buttons_buy(self):
        return self.get_web_elements(self.search_recommended_buttons_buy)

    def amount_of_search_recommended_buttons_in_cart(self):
        return self.amount_of_elements(self.search_recommended_buttons_in_cart)

    def get_first_search_block_buy_button(self):
        return self.get_web_elements(self.first_search_block_buy_button)

    def amount_search_block_button_in_cart(self):
        return len(self.get_web_elements(self.search_block_button_in_cart))

    def list_text_first_search_block_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.first_search_block_price)))
