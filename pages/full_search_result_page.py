from pages.base_page import BasePage
from mixins.mixin_full_search_result import MixinFullSearch_Result


class FullSearchResultPage(BasePage, MixinFullSearch_Result):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinFullSearch_Result.__init__(self)

    @property
    def text_full_search_result_title_block(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.full_search_result_title_block)))

    def click_question_button(self):
        self.click(self.question_button)

    @property
    def text_car_description(self):
        return tuple(map(lambda el: el.text, self.get_web_elements(self.car_description)))

    def click_manafacture(self):
        self.click(self.car_manufacture)

    #def click_sidebar_brand(self):
    #    self.click(self.sidebar_brand)

    #def click_body_brand(self):
    #    self.click(self.body_brand)

    #def click_group(self, group):
    #    item = f'{self.group[0]}', f'{self.group[1].format(group)}'
    #    print(item)
        #self.click(item)


