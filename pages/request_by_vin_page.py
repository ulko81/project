from pages.base_page import BasePage
from mixins.mixin_request_by_vin import MixinRequestByVin


class RequestByVinPage(BasePage, MixinRequestByVin):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinRequestByVin.__init__(driver)

    def click_buy_button(self):
        self.click(self.button_blue)

    @property
    def check_button_in_cart(self):
        return self.get_web_elements(self.button_green)[0]
