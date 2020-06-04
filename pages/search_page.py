from pages.base_page import BasePage
from locators.search_locator import SearchLocator


class SearchPage(BasePage, SearchLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def set_tuple_search_recommended_articules_with_price(self):
        vendor_codes = self.get_web_elements(self.search_recommended_vendor_codes)
        prices = self.get_web_elements(self.search_recommended_prices)
        aricule_with_price = set(zip(map(lambda el: el.text, vendor_codes), map(lambda el: el.text, prices)))
        return list(map(lambda el: el[1], aricule_with_price))

    def get_search_recommended_buttons_buy_blue(self):
        return self.get_web_elements(self.search_recommended_buttons_buy_blue)

    def get_amount_of_search_recommended_buttons_buy_green(self):
        return self.amount_of_elements(self.search_recommended_buttons_buy_green)