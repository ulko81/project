from locators.product_card_locator import ProductCardLocator
from locators.general_locator import GeneralLocator
from pages.base_page import BasePage


class ProductCardPage(ProductCardLocator, BasePage, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_buy(self):
        self.click(self.button_buy_blue)

    def check_present_green_button_buy(self):
        return self.get_web_element(self.button_buy_green)

    def text_card_price(self):
        return self.get_web_element(self.card_price).text

    def get_first_offers_buy_blue_button(self):
        return self.get_web_elements(self.first_offers_buy_blue_button)

    def amount_offers_green_button_buy(self):
        return len(self.get_web_elements(self.button_green))

    def list_text_first_offers_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.first_offers_price)))
