from pages.base_page import BasePage
from mixins.mixin_lax import MixinLax


# laxima
class LaxPage(BasePage, MixinLax):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinLax.__init__(self)

    def check_text_title(self, car_name):
        return self.text_present_in_element(self.title_h1, car_name)
