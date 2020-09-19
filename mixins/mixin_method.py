from helpers.locators import Locators


class MixinMethod:
    def __init__(self):
        self.locators = Locators()
        self.description = self.locators.description
        self.preloader_icon = self.locators.preloader_icon