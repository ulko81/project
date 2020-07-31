from pages.base_page import BasePage
from locators.base_locator import BaseLocator


class SeoPage(BasePage, BaseLocator):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def list_text_breadcrumbs(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.breadcrumbs)))

    @property
    def text_breadcrumbs_last_el(self):
        return self.get_web_element(self.breadcrumbs_last_el).text

    @property
    def list_breadcrumbs_links(self):
        return list(map(lambda el: el.get_attribute('href'), self.get_web_elements(self.breadcrumbs)))

    @property
    def amount_breadcrumbs_devider(self):
        return self.amount_of_elements(self.breadcrumbs_devider)

    @property
    def text_title_h1(self):
        return self.get_web_element(self.base_h1).text

    def click_popular_manafacture(self, car):
        list(filter(lambda el: el.text == car, self.get_web_elements(self.popular_manufactures)))[0].click()

    def click_all_model(self, model):
        list(filter(lambda el: el.text == model, self.get_web_elements(self.cars_block)))[0].click()

    @property
    def text_title_all_models(self):
        return self.get_web_element(self.cars_block_title).text

    @property
    def text_title_all_type_models(self):
        return self.get_web_element(self.cars_block_title).text

