from locators.product_card_locator import ProductCardLocator
from locators.general_locator import GeneralLocator
from pages.base_page import BasePage


class ProductCardPage(ProductCardLocator, BasePage, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_buy(self):
        self.click(self.button_buy_blue)

    def click_to_cart_button(self):
        self.click(self.button_buy_green)

    def check_present_button_in_cart(self):
        return self.get_web_element(self.button_buy_green)

    def text_price(self):
        return self.get_web_element(self.card_price).text

    def get_first_offers_buy_button(self):
        return self.get_web_elements(self.first_offers_buy_button)

    def amount_offers_button_in_cart(self):
        return len(self.get_web_elements(self.button_green))

    def list_text_first_offers_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.first_offers_price)))
