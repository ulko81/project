import requests
from settings.project_setting import TEST_URL
from settings.project_page import project_page
from bs4 import BeautifulSoup
from pages.base_page import BasePage
from locators.base_locator import BaseLocator
from methods.general_method import GeneralMethod
import json


class SEOMethod:

    @staticmethod
    def get_sitemap_links():
        page = requests.get(TEST_URL + project_page.get('sitemap'))
        soup = BeautifulSoup(page.content, 'html.parser')
        #return list(map(lambda el: str(el)[5:].replace('</loc>', ''), soup.find_all('loc')))
        return list(map(lambda loc: loc.text, soup.find_all('loc')))

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
        return description.get_web_element(BaseLocator.base_description).get_attribute('content')

    @staticmethod
    def get_links_from_popular_blocks(url):
        pages_block = []
        popular_block = {
            'manufactures': BaseLocator.popular_manufactures,
            'models': BaseLocator.popular_models,
            'categories': BaseLocator.popular_categories
        }
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for block in popular_block.keys():
            links = list(map(lambda link: link.get('href'), soup.select(popular_block.get(block)[1])))
            pages = list(map(lambda el: url + el, GeneralMethod.get_random_elements(links, 5)))
            pages_block.extend(zip([block for __ in range(0, len(pages))], pages))
        return pages_block

    @staticmethod
    def get_attrs_rel_prev_next(link):
        set_prev_next = set()
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('link', attrs={'rel': True})
        for link in links:
            if link.attrs['rel'][0] == 'next' or link.attrs['rel'][0] == 'prev':
                set_prev_next.add(link.attrs['rel'][0])
        return set_prev_next

    @staticmethod
    def get_microdata_types(url):
        str_microdata_type = ''
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        scripts = soup.select('script[type="application/ld+json"]')
        for script in scripts:
           str_microdata_type += json.loads("".join(script.contents)).get('@type') + '_'
        return str_microdata_type[:-1]

    @staticmethod
    def get_microdata_type(url, types):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        scripts = soup.select('script[type="application/ld+json"]')
        for script in scripts:
           if types == json.loads("".join(script.contents)).get('@type'):
               return json.loads("".join(script.contents))
