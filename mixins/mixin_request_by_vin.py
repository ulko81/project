from helpers.locators import Locators

class MixinRequestByVin:
    def __init__(self):
        self.locators = Locators()
        self.button_blue = self.locators.btn_blue
        self.button_green = self.locators.btn_green
