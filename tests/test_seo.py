import pytest
import requests
from deepdiff import DeepDiff
from methods.seo_method import SEOMethod
from settings.project_setting import TEST_URL, language, test_car
from settings.project_page import *
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.group_page import GroupPage
from methods.general_method import GeneralMethod
from helpers.seo_text import *


class TestSEOSSR:

    @pytest.mark.seo
    @pytest.mark.parametrize('link', SEOMethod.get_sitemap_links(),
                             ids=['sitemap_link {}'.format(link) for link in SEOMethod.get_sitemap_links()])
    def test_sitemap(self, link):
        assert 200 == requests.get(link).status_code

    @pytest.mark.seo
    @pytest.mark.parametrize('page', page_200, ids=['{}{}'.format(TEST_URL, project_page.get(page))
                                                    for page in page_200])
    def test_page_status_200(self, page):
        link = TEST_URL + project_page.get(page)
        assert 200 == requests.get(link).status_code

    @pytest.mark.seo
    @pytest.mark.parametrize('page', seo_page_closed, ids=['{}{}'.format(TEST_URL, project_page.get(page))
                                                           for page in seo_page_closed])
    def test_closed_page(self, page):
        assert '<meta content="noindex, follow" name="robots"/>' == SEOMethod.text_attr_robots(TEST_URL +
                                                                                               project_page.get(page))

    @pytest.mark.seo
    @pytest.mark.parametrize('el', SEOMethod.get_links_from_popular_blocks(TEST_URL), ids=['{} - {}'.format(block, page)
                             for block, page in SEOMethod.get_links_from_popular_blocks(TEST_URL)])
    def test_popular_block(self, el):
        assert 200 == requests.get(el[1]).status_code

    @pytest.mark.seo
    def test__pagination_link_attrs_rel_prev_next(self):
        assert {'prev', 'next'} == SEOMethod.get_attrs_rel_prev_next(TEST_URL + project_page.get('pagination'))


    @pytest.mark.parametrize('page, types', microdata_types.items(),
                             ids=['{}' .format(TEST_URL + project_page.get(page))for page in microdata_types.keys()])
    @pytest.mark.seo
    def test_microdata(self, page, types):
        assert SEOMethod.get_microdata_types(TEST_URL + project_page.get(page)) == types
        assert SEOMethod.get_microdata_type(TEST_URL + project_page.get(page), 'Organization') \
               == microdata_organization.get(TEST_URL)
        assert SEOMethod.get_microdata_type(TEST_URL + project_page.get(page), 'WebSite') \
               == microdata_website.get(TEST_URL)
        if page == 'product_card_with_offers':
            diff = DeepDiff(SEOMethod.get_microdata_type(TEST_URL + project_page.get(page), 'Product'),
                            microdata_product, view='tree')
            assert None == diff.to_dict().get('dictionary_item_removed')


@pytest.mark.usefixtures('get_driver')
class TestSEOCSR(GeneralMethod):

    @pytest.mark.seo
    def test_404(self):
        self.driver.get(TEST_URL + '/page_not_exist')
        assert self.driver.title == '404 Страница, которую вы искали, не найдена'
        assert TEST_URL + project_page.get('404') == self.driver.current_url

    @pytest.mark.seo
    @pytest.mark.parametrize('page', seo_page_title, ids=['{}{}'.format(TEST_URL, project_page.get(page))
                                                          for page in seo_page_title])
    def test_title_ssr_vs_csr(self, page):
        self.driver.get(TEST_URL + project_page.get(page))
        assert self.driver.title == SEOMethod.text_title(TEST_URL + project_page.get(page))
        assert SEOMethod.seo_client_description(self.driver) == SEOMethod.text_description(TEST_URL
                                                                                               + project_page.get(page))

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
        assert self.change_symbols(seo_category_page.text_seo_our_cities, '\n', '') == \
               self.change_symbols(seo_text_our_cities.get(current_language), '\n ', '')


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
        seo = GroupPage(self.driver)
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






