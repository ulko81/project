from pages.base_page import BasePage
from locators.general_locator import GeneralLocator


class FullSearchProductPage(BasePage, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_button_in_cart(self):
        return self.get_web_element(self.button_green)

    def text_price(self):
        return self.get_web_element(self.price).text

