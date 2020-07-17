import pytest
import requests
from methods.seo_method import SEOMethod
from settings.project_setting import TEST_URL
from settings.project_page import *


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
    def test_pagination_prev_next(self):
        pass
        #print(SEOMethod.get_pagination_link(TEST_URL + project_page.get('pagination')))


@pytest.mark.usefixtures('get_driver')
class TestSEOCSR:

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