import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from settings.project_setting import TEST_URL, product, test_car, language, language_to_url
from settings.project_page import project_page
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestSearch(Methods):

    search_category = {
        'RU': 'жидкости охлаждающие и сопутствующие товары',
        'UA': 'рідини охолоджуючі та супутні товари',
        'EN': 'liquid cooling and related products'}

    @pytest.mark.smoke
    @pytest.mark.main
    @pytest.mark.parametrize('search_query', (product.get('upc'), test_car.get('vin')), ids=['parts', 'vin_code'])
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
    @pytest.mark.main
    @pytest.mark.parametrize('current_language', language)
    def test_search_categories(self, current_language):
        self.driver.get(TEST_URL + project_page.get('section'))
        self.change_language(self.driver, current_language)
        section = CatalogPage(self.driver)
        section.fill_search_field(self.search_category.get(current_language))
        section.click_category_in_search_result()
        url = f"{TEST_URL}{language_to_url.get(current_language)}{project_page.get('category')}"
        assert url == self.driver.current_url
