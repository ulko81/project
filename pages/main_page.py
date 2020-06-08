from locators.main_locator import MainLocator
from locators.general_locator import GeneralLocator
from pages.base_page import BasePage


class MainPage(MainLocator, BasePage, GeneralLocator):

    def click_first_buy_button_you_watched(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_button_in_cart_you_watched(self):
        return self.get_web_element(self.button_green)

    def text_price_you_watched(self):
        return self.get_web_element(self.price).text
