from pages.base_page import BasePage
from locators.button import CatalogButton, Button
from locators.text_field import CatalogTextField, TextField


class CatalogPage(BasePage, CatalogButton, Button, CatalogTextField, TextField):

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button(self):
        self.get_web_elements(self.button_blue)[0].click()

    @property
    def check_present_button_in_cart(self):
        return self.get_web_element(self.button_green)

    @property
    def text_first_price(self):
        return self.get_web_elements(self.base_price)[0].text.lower()
