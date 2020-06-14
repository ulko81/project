from pages.base_page import BasePage
from locators.button import MainButton, Button
from locators.text_field import MainTextField, TextField


class MainPage(BasePage, MainButton, Button, MainTextField, TextField):
    def __init__(self, driver):
        super().__init__(driver)

    def click_first_buy_button_you_watched(self):
        self.get_web_elements(self.button_blue)[0].click()

    def check_button_in_cart_you_watched(self):
        return self.get_web_element(self.button_green)

    def text_price_you_watched(self):
        return self.get_web_element(self.base_price).text.lower()
