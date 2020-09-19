import os
import json
import random
import requests

from pages.module_page import ModulePage
from pages.header_page import HeaderPage
from pages.garage_page import GaragePage
from pages.checkout_page import CheckoutPage
from mixins.mixin_method import MixinMethod

from helpers.dict_helper import *
from selenium.webdriver.common.keys import Keys
from settings.project_setting import TEST_URL
from settings.project_page import project_page
from bs4 import BeautifulSoup
from pages.base_page import BasePage
from helpers.locators import Locators


class Methods(MixinMethod):

    def __init__(self):
        MixinMethod.__init__(self)

    @staticmethod
    def add_car(driver, manufacture, model, type_model, modification, mode, year=None):
        add_car = ModulePage(driver)
        my_car = HeaderPage(driver)
        if mode == 'my_car':
            my_car.click_my_car()
        if year:
            add_car.click_years_select(mode)
            add_car.click_car_year_selected(year)
        add_car.click_munufactures_select(mode)
        add_car.fill_manufacture_field(manufacture)
        add_car.click_car_manufacture_selected()
        add_car.click_models_select(mode)
        add_car.click_car_model_selected(model)
        add_car.click_type_models_select(mode)
        add_car.click_car_type_model_selected(type_model)
        add_car.click_modifications_select(mode)
        add_car.click_car_modification_selected(modification)
        add_car.click_select_car()

    @staticmethod
    def change_year_vin(driver, mode, **car_attr):
        if mode == 'module':
            edit_car = ModulePage(driver)
        else:
            edit_car = GaragePage(driver)
        if car_attr.get('year'):
            edit_car.click_edit_car()
            edit_car.clear_year()
            edit_car.fill_year_field(car_attr.get('year'))
            edit_car.click_button_ok_car_year()
        if car_attr.get('vin'):
            edit_car.fill_vin_field(car_attr.get('vin'))
            edit_car.click_button_ok_car_vin()

    @staticmethod
    def delete_chosen_car(driver, mode):
        if mode == 'module':
            delete_car = ModulePage(driver)
        else:
            delete_car = GaragePage(driver)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        delete_car.click_delete_car()
        delete_car.click_confirm_delete_car()

    @staticmethod
    def change_format_date_cart(date):
        if date.find('.') != -1:
            day = int(date[:date.find('.')])
            month = month_cart.get(date[3:5])
            time = date[10:].replace('\n', ' ')
            return '{} {}{}'.format(day, month, time)
        return date.replace('\n', ' ')

    @property
    def get_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import user_login
            return user_login

    @property
    def get_multi_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import multi_user_login
            return multi_user_login

    @property
    def get_password(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_PASS')
        else:
            from settings.user_setting import user_pass
            return user_pass

    def login(self, driver, login=None, password=None):
        if not login:
            login = self.get_username
            password = self.get_password
        header = HeaderPage(driver)
        module = ModulePage(driver)
        header.click_empty_profile()
        module.fill_module_phone_field(login)
        module.fill_module_pass_field(password)
        module.click_module_enter()

    def login_multi(self, driver, login=None, password=None):
        if not login:
            login = self.get_multi_username
            password = self.get_password
        header = HeaderPage(driver)
        module = ModulePage(driver)
        header.click_empty_profile()
        module.fill_module_phone_field(login)
        module.fill_module_pass_field(password)
        module.click_module_enter()
        button = header.get_first_multi_users()
        button.click()

    def login_checkout(self, driver, login=None, password=None):
        if not login:
            login = self.get_username
            password = self.get_password
        checkout = CheckoutPage(driver)
        checkout.fill_checkout_phone_field(login)
        checkout.fill_checkout_pass_field(password)
        checkout.click_checkout_enter()

    def login_multi_checkout(self, driver, login=None, password=None):
        if not login:
            login = self.get_multi_username
            password = self.get_password
        checkout = CheckoutPage(driver)
        checkout.fill_checkout_phone_field(login)
        checkout.fill_checkout_pass_field(password)
        checkout.click_checkout_enter()
        button = checkout.get_first_multi_users()
        button.click()

    @staticmethod
    def change_language(driver, selected_language):
        language = HeaderPage(driver)
        current_language = language.text_current_language
        if current_language != selected_language:
            language.click_language_select()
            language.click_module_language_option(selected_language)

    def wait_client_loader(self, driver):
        timeout = 10
        preloader = BasePage(driver, timeout)
        try:
            preloader.get_visible_element(self.preloader_icon)
        except Exception:
            pass
        preloader.check_invisible_element(self.preloader_icon)

    @staticmethod
    def change_format_price(price):
        if language_cur.get('ru') in price:
            count = price.find(language_cur.get('ru')) + 3
            price = price[:count]
            return price

    @staticmethod
    def get_vendor_code(trademark, trademark_with_vendor_code):
        return trademark_with_vendor_code.replace(trademark, '').strip()

    @staticmethod
    def get_random_elements(old_list, qnt):
        new_list = []
        if len(old_list) > qnt:
            for i in range(qnt):
                new_list.append(old_list[random.randint(0, len(old_list) - 1)])
            return new_list
        return old_list

    @staticmethod
    def change_symbols(string, old_symbols, new_symbols):
        return string.replace(old_symbols, new_symbols)

    @staticmethod
    def clear_field(driver, locator):
        field = BasePage(driver)
        return field.get_web_element(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def close_draggable(self, driver):
        timeout = 10
        draggable = BasePage(driver, timeout)
        try:
            pass
            # draggable.get_first_visible_element(self.icon_close_draggable).click()
        except Exception:
            pass

    @staticmethod
    def get_sitemap_links():
        page = requests.get(TEST_URL + project_page.get('sitemap'))
        soup = BeautifulSoup(page.content, 'html.parser')
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
        return description.get_web_element(Locators.description).get_attribute('content')

    def get_links_from_popular_blocks(self, url):
        pages_block = []
        popular_block = {
            'manufactures': Locators.popular_manufactures,
            'models': Locators.popular_models,
            'categories': Locators.popular_categories
        }
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for block in popular_block.keys():
            links = list(map(lambda link: link.get('href'), soup.select(popular_block.get(block)[1])))
            pages = list(map(lambda el: url + el, self.get_random_elements(links, 5)))
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

    def get_microdata_breadcrumbs(self, url):
        return list(map(lambda el: el.get('item').get('name'),
                        self.get_microdata_type(url, 'BreadcrumbList').get('itemListElement')))
