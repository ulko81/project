import json
import random
import requests
from bs4 import BeautifulSoup
from helpers.general_data import *
from settings.project_setting import TEST_URL
from helpers.project_page import project_page


def change_format_date_cart(date):
    if date.find('.') != -1:
        day = int(date[:date.find('.')])
        month = month_cart.get(date[3:5])
        time = date[10:].replace('\n', ' ')
        return '{} {}{}'.format(day, month, time)
    return date.replace('\n', ' ')


def change_format_price(price):
    if language_cur.get('ru') in price:
        count = price.find(language_cur.get('ru')) + 3
        price = price[:count]
        return price


def get_vendor_code(trademark, trademark_with_vendor_code):
        return trademark_with_vendor_code.replace(trademark, '').strip()


def get_random_elements(old_list, qnt):
    new_list = []
    if len(old_list) > qnt:
        for i in range(qnt):
            new_list.append(old_list[random.randint(0, len(old_list) - 1)])
        return new_list
    return old_list


def change_symbols(string, old_symbols, new_symbols):
    return string.replace(old_symbols, new_symbols)


def get_sitemap_links():
    page = requests.get(TEST_URL + project_page.get('sitemap'))
    soup = BeautifulSoup(page.content, 'html.parser')
    return list(map(lambda loc: loc.text, soup.find_all('loc')))


def text_attr_robots(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return str(soup.find('meta', attrs={'name': 'robots'}))


def text_title(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return str(soup.find('title').text)


def text_description(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return str(soup.find('meta', attrs={'name': 'description'}).attrs['content'])


def get_attrs_rel_prev_next(link):
    set_prev_next = set()
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('link', attrs={'rel': True})
    for link in links:
        if link.attrs['rel'][0] == 'next' or link.attrs['rel'][0] == 'prev':
            set_prev_next.add(link.attrs['rel'][0])
    return set_prev_next


def get_microdata_types(url):
    str_microdata_type = ''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    scripts = soup.select('script[type="application/ld+json"]')
    for script in scripts:
        str_microdata_type += json.loads("".join(script.contents)).get('@type') + '_'
    return str_microdata_type[:-1]


def get_microdata_type(url, types):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    scripts = soup.select('script[type="application/ld+json"]')
    for script in scripts:
        if types == json.loads("".join(script.contents)).get('@type'):
            return json.loads("".join(script.contents))


def get_microdata_breadcrumbs(url):
    return list(map(lambda el: el.get('item').get('name'),
                    get_microdata_type(url, 'BreadcrumbList').get('itemListElement')))
