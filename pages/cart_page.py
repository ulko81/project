from pages.base_page import BasePage
from locators.cart_locator import CartLocator
from locators.general_locator import GeneralLocator


class CartPage(BasePage, CartLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button_recomended(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_present_button_in_cart_recomended(self):
        return self.get_web_element(self.button_green)

    def text_price(self):
        return self.get_web_elements(self.price)[0].text.replace('.0', '')






