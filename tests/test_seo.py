import pytest
import requests
from methods.seo_method import SEOMethod


class TestSitemap:

    @pytest.mark.seo
    @pytest.mark.parametrize('link', SEOMethod.get_sitemap_links(),
                             ids=['sitemap_link {}'.format(link) for link in SEOMethod.get_sitemap_links()])
    def test_sitemap(self, link):
        assert 200 == requests.get(link).status_code

