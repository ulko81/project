import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.full_search_result_page import FullSearchResultPage
from pages.lax_page import LaxPage
from settings.project_setting import TEST_URL, product, test_car, car_description
from helpers.project_page import project_page
from helpers.general_data import language, language_to_url
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestSearch(Methods):
    car_name_laxima = 'TOYOTA YARIS/HYBRID'
    search_result_side = 'sidebar', 'body'
    brand = 'bosch'
    search_query_for_titles = {
        'brand': brand,
        'spare_part': product.get('upc'),
        'manufacture': test_car.get('manufacture'),
        'model': test_car.get('model'),
    }

    titles_search_result = {
        'brand': {
            'RU': ('БРЕНДЫ', 'РАЗДЕЛЫ И ГРУППЫ', 'КАТЕГОРИИ', 'БРЕНДЫ', 'КАТЕГОРИИ', 'ТОВАРЫ ПО НАЗВАНИЮ И ОПИСАНИЮ'),
            'UA': ('БРЕНДИ', 'РОЗДІЛИ І ГРУПИ', 'КАТЕГОРІЇ', 'БРЕНДИ', 'КАТЕГОРІЇ', 'ТОВАРИ ЗА НАЗВОЮ ТА ОПИСОМ'),
            'EN': ('TRADEMARKS', 'SECTIONS AND GROUPS', 'CATEGORIES', 'TRADEMARKS', 'CATEGORIES',
                   'NAME AND DESCRIPTION OF GOODS')},
        'spare_part': {
            'RU': ('КАТЕГОРИИ', 'ТОВАРЫ ПО НОМЕРУ', 'КАТЕГОРИИ', 'ТОВАРЫ ПО НАЗВАНИЮ И ОПИСАНИЮ'),
            'UA': ('КАТЕГОРІЇ', 'ТОВАРИ ЗА НОМЕРОМ', 'КАТЕГОРІЇ', 'ТОВАРИ ЗА НАЗВОЮ ТА ОПИСОМ'),
            'EN': ('CATEGORIES', 'PRODUCTS BY ARTICLE NUMBER', 'CATEGORIES', 'NAME AND DESCRIPTION OF GOODS')},
        'manufacture': {
            'RU': ('РАЗДЕЛЫ И ГРУППЫ', 'КАТЕГОРИИ ДЛЯ ТОЙОТА', 'ТОВАРЫ ПО НОМЕРУ',
                   'КАТЕГОРИИ ДЛЯ ТОЙОТА ЗАПЧАСТИ ДЛЯ ТОЙОТА', 'ТОВАРЫ ПО НАЗВАНИЮ И ОПИСАНИЮ'),
            'UA': ('РОЗДІЛИ І ГРУПИ', 'КАТЕГОРІЇ ДЛЯ ТОЙОТА', 'ТОВАРИ ЗА НОМЕРОМ',
                   'КАТЕГОРІЇ ДЛЯ ТОЙОТА ЗАПЧАСТИНИ ДЛЯ ТОЙОТА', 'ТОВАРИ ЗА НАЗВОЮ ТА ОПИСОМ'),
            'EN': ('SECTIONS AND GROUPS', 'CATEGORIES FOR TOYOTA', 'PRODUCTS BY ARTICLE NUMBER',
                   'CATEGORIES FOR TOYOTA PARTS FOR TOYOTA', 'NAME AND DESCRIPTION OF GOODS')},
        'model': {
            'RU': ('РАЗДЕЛЫ И ГРУППЫ', 'КАТЕГОРИИ ДЛЯ ТОЙОТА ЯРИС',
                   'КАТЕГОРИИ ДЛЯ ТОЙОТА ЯРИСЗАПЧАСТИ ДЛЯ ТОЙОТА ЯРИС', 'ТОВАРЫ ПО НАЗВАНИЮ И ОПИСАНИЮ'),
            'UA': ('РОЗДІЛИ І ГРУПИ', 'КАТЕГОРІЇ ДЛЯ ТОЙОТА ЯРІС',
                   'КАТЕГОРІЇ ДЛЯ ТОЙОТА ЯРІСЗАПЧАСТИНИ ДЛЯ ТОЙОТА ЯРІС', 'ТОВАРИ ЗА НАЗВОЮ ТА ОПИСОМ'),
            'EN': ('SECTIONS AND GROUPS', 'CATEGORIES FOR TOYOTA YARIS',
                   'CATEGORIES FOR TOYOTA YARISPARTS FOR TOYOTA YARIS', 'NAME AND DESCRIPTION OF GOODS')},
    }

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('search_query', (product.get('upc'), test_car.get('vin')), ids=['spare_part', 'vin_code'])
    def test_simple_search(self, search_query):
        main = MainPage(self.driver)
        self.driver.get(TEST_URL)
        main.click_search_field()
        main.fill_search_field(search_query)
        assert main.check_search_full_result()
        main.click_search_button()
        url = f"{TEST_URL}/search/?query={search_query}"
        assert self.driver.current_url == url

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('current_language', language)
    def test_search_categories(self, current_language):

        search_category = {
            'RU': 'жидкости охлаждающие и сопутствующие товары',
            'UA': 'рідини охолоджуючі та супутні товари',
            'EN': 'liquid cooling and related products'}

        self.driver.get(TEST_URL + project_page.get('section'))
        self.change_language(self.driver, current_language)
        section = CatalogPage(self.driver)
        section.fill_search_field(search_category.get(current_language))
        section.click_category_in_search_result()
        url = f"{TEST_URL}{language_to_url.get(current_language)}{project_page.get('category')}"
        assert url == self.driver.current_url

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('current_language', language)
    def test_full_search_vin_click_question(self, current_language):
        expected_car_type = f"{self.car_name_laxima}: {test_car.get('vin')}"
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        main.click_search_field()
        main.fill_search_field(test_car.get('vin'))
        assert main.check_search_full_result()
        actual_car_type = full_search_result.text_full_search_result_title_block
        assert actual_car_type[0] == expected_car_type
        full_search_result.click_question_button()
        actual_car_description = full_search_result.text_car_description
        assert len(actual_car_description) == len(car_description.get(current_language))
        for i in range(len(car_description.get(current_language))):
            assert car_description.get(current_language)[i] == actual_car_description[i]

    @pytest.mark.smoke
    @pytest.mark.search
    def test_full_search_vin_click_car(self):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        lax = LaxPage(self.driver)
        self.driver.get(TEST_URL)
        main.click_search_field()
        main.fill_search_field(test_car.get('vin'))
        assert main.check_search_full_result()
        full_search_result.click_manafacture()
        assert lax.check_text_title(self.car_name_laxima)

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('query_type', search_query_for_titles.keys())
    def test_full_search_block_title(self, current_language, query_type):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        main.click_search_field()
        main.fill_search_field(self.search_query_for_titles.get(query_type))
        assert main.check_search_full_result()
        expected_title_blocks = self.titles_search_result.get(query_type).get(current_language)
        actual_title_blocks = full_search_result.text_full_search_result_title_block
        print(f"{query_type} - {current_language} {actual_title_blocks}")
        assert len(actual_title_blocks) == len(expected_title_blocks)
        for i in range(len(expected_title_blocks)):
            assert actual_title_blocks[i] == expected_title_blocks[i]

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('side', search_result_side)
    def test_full_search_result_click_brand(self, side):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        self.driver.get(TEST_URL)
        main.click_search_field()
        main.fill_search_field(self.brand)
        full_search_result.click_brand(side)
        url = f"{TEST_URL}/{self.brand}-brand/"
        assert url == self.driver.current_url

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('current_language', language)
    def test_full_search_result_click_group(self, current_language):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        group = CatalogPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        main.click_search_field()
        main.fill_search_field(self.brand)
        expected_group_name = full_search_result.text_first_group.strip()
        expected_group_url = full_search_result.url_first_group
        full_search_result.click_first_group()
        assert group.check_title(expected_group_name.upper())
        assert expected_group_url == self.driver.current_url

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('side', search_result_side)
    def test_full_search_result_click_category(self, current_language, side):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        category = CatalogPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        main.click_search_field()
        main.fill_search_field(self.brand)
        expected_category_name = f"{full_search_result.text_first_category(side).upper()} {self.brand.upper()}"
        expected_category_url = full_search_result.url_first_category(side)
        full_search_result.click_first_category(side)
        assert category.check_title(expected_category_name)
        assert expected_category_url == self.driver.current_url
