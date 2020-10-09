from helpers.locators import Locators


class MixinFullSearch_Result:
    def __init__(self):
        self.locators = Locators()
        self.full_search_result_title_block = self.locators.multi_search_results_block_title
        self.question_button = self.locators.unit_map_info_button
        self.car_description = self.locators.modal_tooltip_faq
        self.car_manufacture = self.locators.grid_table_manufacture
        self.sidebar_brand = self.locators.multi_search_sidebar_brand
        self.body_brand = self.locators.multi_search_body_brand
        self.group = self.locators.multi_search_sidebar_section
        self.sidebar_category_name = self.locators.multi_search_sidebar_category_name
        self.sidebar_category_link = self.locators.multi_search_sidebar_category_link
        self.body_category = self.locators.multi_search_body_category
