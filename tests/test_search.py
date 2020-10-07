import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.full_search_result_page import FullSearchResultPage
from pages.lax_page import LaxPage
from settings.project_setting import TEST_URL, product, test_car, language, language_to_url
from settings.project_page import project_page
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestSearch(Methods):
    brand = 'bosch'
    category = 'охлаждающие'
    search_result_side = 'sidebar', 'body'

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
    def test_full_search_vin(self, current_language):

        expected_car_type = f"TOYOTA YARIS/HYBRID: {test_car.get('vin')}"
        car_description = {
            'RU': ('Модель: KSP130L-CHMRKW', 'Описание: KSP130,NHP130,NLP130,NSP130', 'Дата: 01.2012',
                   'Цвет кузова: 068', 'Цвет салона: FA11', 'laximo.prodPeriod: 07.2011 - 07.2014',
                   "Опции: ATM,MTM: MANUAL TRANSMISSION; NO. of doors: 5-DOOR; Driver's position: "
                   "LEFT-HAND DRIVE VEHICLES; Grade: STANDARD TYPE; Engine: (1KRFE) 1000CC 12-VALVE DOHC EFI; "
                   "Gear shift type: MTM, 5-SPEED FLOOR SHIFT"),
            'UA': ('Модель: KSP130L-CHMRKW', 'Опис: KSP130,NHP130,NLP130,NSP130', 'Дата: 01.2012',
                   'Колір кузова: 068', 'Колір салона: FA11', 'laximo.prodPeriod: 07.2011 - 07.2014',
                   "Опції: ATM,MTM: MANUAL TRANSMISSION; NO. of doors: 5-DOOR; Driver's position: LEFT-HAND DRIVE "
                   "VEHICLES; Grade: STANDARD TYPE; Engine: (1KRFE) 1000CC 12-VALVE DOHC EFI; Gear shift type: MTM, "
                   "5-SPEED FLOOR SHIFT"),
            'EN': ('Model: KSP130L-CHMRKW', 'Description: KSP130,NHP130,NLP130,NSP130', 'Date: 01.2012',
                   'Body color: 068', 'Interior color: FA11', 'laximo.prodPeriod: 07.2011 - 07.2014',
                   "Options: ATM,MTM: MANUAL TRANSMISSION; NO. of doors: 5-DOOR; Driver's position: LEFT-HAND "
                   "DRIVE VEHICLES; Grade: STANDARD TYPE; Engine: (1KRFE) 1000CC 12-VALVE DOHC EFI; Gear shift type: "
                   "MTM, 5-SPEED FLOOR SHIFT")

        }
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
    @pytest.mark.parametrize('current_language', language)
    def test_full_search_block_title(self, current_language):

        title_blocks = {
            'RU': ('БРЕНДЫ', 'РАЗДЕЛЫ И ГРУППЫ', 'КАТЕГОРИИ', 'БРЕНДЫ', 'КАТЕГОРИИ', 'ТОВАРЫ ПО НАЗВАНИЮ И ОПИСАНИЮ'),
            'UA': ('БРЕНДИ', 'РОЗДІЛИ І ГРУПИ', 'КАТЕГОРІЇ', 'БРЕНДИ', 'КАТЕГОРІЇ', 'ТОВАРИ ЗА НАЗВОЮ ТА ОПИСОМ'),
            'EN': ('TRADEMARKS', 'SECTIONS AND GROUPS', 'CATEGORIES', 'TRADEMARKS', 'CATEGORIES',
                   'NAME AND DESCRIPTION OF GOODS')
        }
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        main.click_search_field()
        main.fill_search_field(self.brand)
        assert main.check_search_full_result()
        expected_title_blocks = title_blocks.get(current_language)
        actual_title_blocks = full_search_result.text_full_search_result_title_block
        assert len(actual_title_blocks) == len(expected_title_blocks)
        for i in range(len(expected_title_blocks)):
            assert actual_title_blocks[i] == expected_title_blocks[i]

    @pytest.mark.smoke
    @pytest.mark.search
    def test_full_search_block_click_car(self):
        car_name_laxima = 'TOYOTA YARIS/HYBRID'
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        lax = LaxPage(self.driver)
        self.driver.get(TEST_URL)
        main.click_search_field()
        main.fill_search_field(test_car.get('vin'))
        assert main.check_search_full_result()
        full_search_result.click_manafacture()
        assert lax.check_text_title(car_name_laxima)

    @pytest.mark.smoke
    @pytest.mark.search
    @pytest.mark.parametrize('side', search_result_side)
    def test_full_search_result_click_brand(self, side):
        main = MainPage(self.driver)
        full_search_result = FullSearchResultPage(self.driver)
        self.driver.get(TEST_URL)
        main.click_search_field()
        main.fill_search_field(self.brand)
        full_search_result.click_sidebar_brand() if side == 'sidebar' else full_search_result.click_body_brand()
        url = f"{TEST_URL}/{self.brand}-brand/{TEST_URL}"
        assert url == self.driver.current_url

    #@pytest.mark.smoke
    #@pytest.mark.search
    #def test_full_search_result_click_group(self):

    #    full_search_group = {
    #        'RU': ('жидкости', 'Жидкости'),
    #        'UA': ('рідини', 'Рідини'),
    #        'EN': ('liquids and fluids', 'Liquids and fluids')
    #    }
    #    main = MainPage(self.driver)
    #    full_search_result = FullSearchResultPage(self.driver)
    #    self.driver.get(TEST_URL)
    #    main.click_search_field()
    #    main.fill_search_field(full_search_group.get('RU')[0])
    #    full_search_result.click_group(full_search_group.get('RU')[1])
        #assert url == self.driver.current_url
