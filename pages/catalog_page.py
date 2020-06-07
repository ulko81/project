from pages.base_page import BasePage
from locators.catalog_locator import CatalogLocator
from locators.general_locator import GeneralLocator


class CatalogPage(BasePage, CatalogLocator, GeneralLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_present_green_button_buy(self):
        return self.get_web_element(self.button_green)

    def text_first_price(self):
        return self.get_web_elements(self.price)[0].text
