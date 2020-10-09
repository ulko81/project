import pytest
import requests
from deepdiff import DeepDiff
from settings.project_setting import TEST_URL, test_car, product
from helpers.general_data import language, language_to_url
from helpers.project_page import *
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.card_page import CardPage
from pages.seo_page import SeoPage
from helpers.seo_data import *
from helpers.functions import get_sitemap_links, text_attr_robots, get_attrs_rel_prev_next, get_microdata_type, \
    get_microdata_types, text_title, text_description, get_microdata_breadcrumbs, change_symbols
from helpers.methods import Methods


class TestSEOSSR:

    @pytest.mark.smoke
    @pytest.mark.seo
    @pytest.mark.parametrize('link', get_sitemap_links(), ids=[f'sitemap_link {link}' for link in get_sitemap_links()])
    def test_sitemap(self, link):
        assert 200 == requests.get(link).status_code

    @pytest.mark.smoke
    @pytest.mark.seo
    @pytest.mark.parametrize('page', page_200, ids=[f'{page}: {TEST_URL + project_page.get(page)}'for page in page_200])
    def test_page_status_200(self, page):
        link = TEST_URL + project_page.get(page)
        assert 200 == requests.get(link).status_code

    @pytest.mark.smoke
    @pytest.mark.seo
    @pytest.mark.parametrize('page', seo_page_noindex_follow, ids=[f'{page}: {TEST_URL + project_page.get(page)}'
                             for page in seo_page_noindex_follow])
    def test_closed_page_follow(self, page):
        assert '<meta content="noindex, follow" name="robots"/>' == text_attr_robots(TEST_URL + project_page.get(page))

    @pytest.mark.smoke
    @pytest.mark.seo
    @pytest.mark.parametrize('page', seo_page_noindex_nofollow, ids=[f'{page}: {TEST_URL + project_page.get(page)}'
                             for page in seo_page_noindex_nofollow])
    def test_closed_page_nofollow(self, page):
        assert '<meta content="noindex, nofollow" name="robots"/>' == text_attr_robots(TEST_URL +
                                                                                       project_page.get(page))

    @pytest.mark.seo
    @pytest.mark.parametrize('el', Methods.get_links_from_popular_blocks(TEST_URL), ids=[f'{block}: {page}'
                             for block, page in Methods.get_links_from_popular_blocks(TEST_URL)])
    def test_popular_block(self, el):
        assert 200 == requests.get(el[1]).status_code

    @pytest.mark.seo
    def test__pagination_link_attrs_rel_prev_next(self):
        assert {'prev', 'next'} == get_attrs_rel_prev_next(TEST_URL + project_page.get('pagination'))

    @pytest.mark.parametrize('page, types', microdata_types.items(),
                             ids=[f'{page}: {TEST_URL + project_page.get(page)}'
                                  for page in microdata_types.keys()])
    @pytest.mark.smoke
    @pytest.mark.seo
    def test_microdata(self, page, types):
        assert get_microdata_types(TEST_URL + project_page.get(page)) == types
        assert get_microdata_type(TEST_URL + project_page.get(page), 'Organization') \
               == microdata_organization.get(TEST_URL)
        assert get_microdata_type(TEST_URL + project_page.get(page), 'WebSite') == microdata_website.get(TEST_URL)
        if page == 'product_card_with_offers':
            diff = DeepDiff(get_microdata_type(TEST_URL + project_page.get(page), 'Product'),
                            microdata_product, view='tree')
            assert None == diff.to_dict().get('dictionary_item_removed')

    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('page, breadcrumbs_microdata', breadcrumbs.items(),
                             ids=['{}: {}'.format(page, TEST_URL + project_page.get(page))
                                  for page in breadcrumbs.keys()])
    @pytest.mark.seo
    @staticmethod
    def test_microdata_breadcrumbs(page, breadcrumbs_microdata, current_language):
        if page != 'laxima_spare':
            expected_breadcrumbs = breadcrumbs_microdata.get(current_language)
            actual_microdata_breadcrumbs = get_microdata_breadcrumbs(TEST_URL + language_to_url.get(current_language)
                                                                     + project_page.get(page))
            assert len(actual_microdata_breadcrumbs) == len(expected_breadcrumbs)
            for el in range(len(actual_microdata_breadcrumbs)):
                assert actual_microdata_breadcrumbs[el] == expected_breadcrumbs[el]


@pytest.mark.usefixtures('get_driver')
class TestSEOCSR(Methods):

    @pytest.mark.seo
    def test_404(self):
        self.driver.get(TEST_URL + '/page_not_exist')
        assert self.driver.title == '404 Страница, которую вы искали, не найдена'
        assert TEST_URL + project_page.get('404') == self.driver.current_url

    @pytest.mark.seo
    @pytest.mark.parametrize('page', seo_page_title, ids=[f'{page}: {TEST_URL + project_page.get(page)}'
                                                          for page in seo_page_title])
    def test_title_ssr_vs_csr(self, page):
        self.driver.get(TEST_URL + project_page.get(page))
        assert self.driver.title == text_title(TEST_URL + project_page.get(page))
        assert self.seo_client_description(self.driver) == text_description(TEST_URL + project_page.get(page))

    @pytest.mark.seo
    def test_seo_text_after_autogid(self):
        seo_main_page = MainPage(self.driver)
        self.driver.get(TEST_URL)
        assert 'Эксплуатация автомобилей в Украине' in seo_main_page.text_seo_after_autogid

    @pytest.mark.seo
    @pytest.mark.parametrize('current_language', language)
    def test_seo_text_in_category_page(self, current_language):
        seo_category_page = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('category'))
        self.change_language(self.driver, current_language)
        assert change_symbols(seo_category_page.text_seo_our_cities, '\n', '') == \
               change_symbols(seo_text_our_cities.get(current_language), '\n ', '')

    @pytest.mark.seo
    def test_avtogid_selection_tabs(self):
        autogid = MainPage(self.driver)
        self.driver.get(TEST_URL)
        for count, guide_tab in enumerate(autogid.get_guide_tabs):
            if count == 0:
                assert guide_tab.text == autogid.text_guide_tab_selected
            else:
                guide_tab.click()
                assert guide_tab.text == autogid.text_guide_tab_selected

    @pytest.mark.seo
    @pytest.mark.parametrize('current_language', language)
    def test_redirect_car_data(self, current_language):
        seo = SeoPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('group'))
        self.change_language(self.driver, current_language)
        seo.click_popular_manafacture(test_car.get('manufacture'))
        assert test_car.get('manufacture_slug') in self.driver.current_url
        assert seo.text_title_all_models == all_type_manafactures.get(current_language)
        assert seo.text_title_h1.strip() == h1_group_on_manafacture.get(current_language)
        seo.click_all_model(test_car.get('model'))
        assert test_car.get('model_slug') in self.driver.current_url
        assert seo.text_title_all_type_models == all_type_models.get(current_language)
        assert seo.text_title_h1.strip() == h1_group_on_model.get(current_language)

    @pytest.mark.seo
    def test_cart_attribute_redirect(self):
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        link = card.get_link_first_attribute_value
        card.click_first_attribute_value()
        assert self.driver.current_url == link

    @pytest.mark.seo
    @pytest.mark.parametrize('current_language', language)
    def test_category_block_all_type_model(self, current_language):
        catalog = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('catalog_with_car_model'))
        self.change_language(self.driver, current_language)
        assert catalog.text_title_all_type_models == all_type_models.get(current_language)

    @pytest.mark.seo
    def test_refresh_catalog_page(self):
        self.driver.get(TEST_URL + project_page.get('catalog_with_filter'))
        self.driver.refresh()
        assert self.driver.title != '404 Страница, которую вы искали, не найдена'
        assert TEST_URL + project_page.get('404') != self.driver.current_url

    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('page, breadcrumbs', breadcrumbs.items(),
                             ids=['{}: {}' .format(page, TEST_URL + project_page.get(page))
                                  for page in breadcrumbs.keys()])
    @pytest.mark.seo
    def test_breadscrumbs(self, page, breadcrumbs, current_language):
        seo = SeoPage(self.driver)
        self.driver.get(TEST_URL + project_page.get(page))
        self.change_language(self.driver, current_language)
        actual_breadcrumbs = seo.list_text_breadcrumbs[1:]
        if page != 'product_card_with_offers':
            last_el = seo.text_breadcrumbs_last_el
            actual_breadcrumbs.append(last_el)
        expected_breadcrumbs = breadcrumbs.get(current_language)
        assert len(actual_breadcrumbs) == len(expected_breadcrumbs)
        for el in range(len(actual_breadcrumbs)):
            assert actual_breadcrumbs[el] == expected_breadcrumbs[el]

    @pytest.mark.seo
    def test_breadscrumbs_links(self):
        pages = ('main', 'section', 'group', 'category', 'catalog_with_filter', 'catalog_with_filter_and_car',
                 'catalog_with_filter_and_model')
        seo = SeoPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('catalog_with_filter_and_type_model'))
        actual_links = seo.list_breadcrumbs_links
        expected_links = tuple(map(lambda page: TEST_URL + project_page.get(page), pages))
        assert len(actual_links) == len(expected_links)
        assert len(actual_links) == seo.amount_breadcrumbs_devider
        for el in range(len(actual_links)):
            assert actual_links[el] == expected_links[el]

    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.seo
    def test_card_h1(self, current_language):
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        self.change_language(self.driver, current_language)
        seo = SeoPage(self.driver)
        h1 = seo.text_title_h1
        assert f"{product.get('brand')} {product.get('upc')}" in h1
        assert product.get('ware_just_num') in h1
