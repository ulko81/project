from locators.product_card_locator import ProductCardLocator
from pages.base_page import BasePage


class ProductCardPage(ProductCardLocator, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_buy(self):
        return self.click(self.button_buy_blue)

    def check_present_green_button_buy(self):
        return self.get_web_element(self.button_buy_green)

    def text_card_price(self):
        return self.get_web_element(self.card_price).text