from pages.base_page import BasePage
from mixins.mixin_full_search_result import MixinFullSearchResult


class FullSearchResultPage(BasePage, MixinFullSearchResult):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinFullSearchResult.__init__(self)

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

    def click_brand(self, side):
        self.click(self.sidebar_brand) if side == 'sidebar' else self.click(self.body_brand)

    def click_body_brand(self):
        self.click(self.body_brand)

    def click_first_group(self):
        self.get_first_visible_element(self.group).click()

    @property
    def text_first_group(self):
        return self.get_first_visible_element(self.group).text

    @property
    def url_first_group(self):
        return self.get_first_visible_element(self.group).get_attribute('href')

    def text_first_category(self, side):
        return self.get_first_visible_element(self.sidebar_category_name).text if side == 'sidebar' else \
            self.get_first_visible_element(self.body_category).text

    def url_first_category(self, side):
        return self.get_first_visible_element(self.sidebar_category_link).get_attribute('href')if side == 'sidebar' else \
            self.get_first_visible_element(self.body_category).get_attribute('href')

    def click_first_category(self, side):
        self.click(self.sidebar_category_link)if side == 'sidebar' else self.click(self.body_category)

    def click_more_button_categories(self):
        self.click(self.more_button_categories)

    def click_more_button_products(self):
        self.click(self.more_button_products)
