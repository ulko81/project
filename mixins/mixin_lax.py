from helpers.locators import Locators


class MixinLax:
    def __init__(self):
        self.locators = Locators()
        self.title_h1 = self.locators.h1
