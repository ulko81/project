from pages.base_page import BasePage
from locators.request_by_vin_locator import RequestByVinLocator


class RequestByVinPage(BasePage, RequestByVinLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_buy_button(self):
        self.click(self.button_blue)

    @property
    def check_button_in_cart(self):
        return self.get_web_elements(self.button_green)[0]
