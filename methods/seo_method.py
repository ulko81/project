import requests
from settings.project_setting import TEST_URL
from settings.project_page import project_page
from bs4 import BeautifulSoup
from locators.text_field import TextField
from pages.base_page import BasePage
from methods.general_func import get_random_elements
from locators.link import Link


class SEOMethod:

    @staticmethod
    def get_sitemap_links():
        page = requests.get(TEST_URL + project_page.get('sitemap'))
        soup = BeautifulSoup(page.content, 'html.parser')
        return list(map(lambda el: str(el)[5:].replace('</loc>', ''), soup.find_all('loc')))

    @staticmethod
    def text_attr_robots(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        return str(soup.find('meta', attrs={'name': 'robots'}))

    @staticmethod
    def text_title(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        return str(soup.find('title').text)

    @staticmethod
    def text_description(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        return str(soup.find('meta', attrs={'name': 'description'}).attrs['content'])

    @staticmethod
    def seo_client_description(driver):
        description = BasePage(driver)
        return description.get_web_element(TextField.base_description).get_attribute('content')

    @staticmethod
    def get_links_from_popular_blocks(url):
        pages_block = []
        popular_block = {
            'manufactures': Link.popular_manufactures,
            'models': Link.popular_models,
            'categories': Link.popular_categories
        }
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for block in popular_block.keys():
            links = list(map(lambda link: link.get('href'), soup.select(popular_block.get(block)[1])))
            pages = list(map(lambda el: url + el, get_random_elements(links, 5)))
            pages_block.extend(zip([block for __ in range(0, len(pages))], pages))
        return pages_block
