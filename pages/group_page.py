from pages.base_page import BasePage
from locators.header_locator import BaseLocator


class GroupPage(BasePage, BaseLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_popular_manafacture(self, car):
        list(filter(lambda el: el.text == car, self.get_web_elements(self.popular_manufactures)))[0].click()

    def click_all_model(self, model):
        list(filter(lambda el: el.text == model, self.get_web_elements(self.cars_block)))[0].click()

    @property
    def text_title_all_models(self):
        return self.get_web_element(self.cars_block_title).text

    @property
    def text_title_h1(self):
        return self.get_web_element(self.base_h1).text

    @property
    def text_title_all_type_models(self):
        return self.get_web_element(self.cars_block_title).text

