import requests
from settings.project_setting import TEST_URL, project_page
from bs4 import BeautifulSoup


class SEOMethod:

    @staticmethod
    def get_sitemap_links():
        page = requests.get(TEST_URL + project_page.get('sitemap'))
        soup = BeautifulSoup(page.content, 'html.parser')
        return list(map(lambda el: str(el)[5:].replace('</loc>', ''), soup.find_all('loc')))

