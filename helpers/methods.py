import os
import requests
from bs4 import BeautifulSoup
from pages.base_page import BasePage
from pages.module_page import ModulePage
from pages.header_page import HeaderPage
from pages.garage_page import GaragePage
from pages.checkout_page import CheckoutPage
from helpers.locators import Locators
from helpers.functions import get_random_elements


class Methods:

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

    @staticmethod
    def wait_client_loader(driver):
        timeout = 10
        preloader = BasePage(driver, timeout)
        try:
            preloader.get_visible_element(Locators.preloader_icon)
        except Exception:
            pass
        preloader.check_invisible_element(Locators.preloader_icon)

    @staticmethod
    def close_draggable(driver):
        timeout = 10
        draggable = BasePage(driver, timeout)
        try:
            pass
            # draggable.get_first_visible_element(Locators.icon_close_draggable).click()
        except Exception:
            pass

    @staticmethod
    def seo_client_description(driver):
        description = BasePage(driver)
        return description.get_web_element(Locators.description).get_attribute('content')

    @staticmethod
    def get_links_from_popular_blocks(url):
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
            pages = list(map(lambda el: url + el, get_random_elements(links, 5)))
            pages_block.extend(zip([block for __ in range(0, len(pages))], pages))
        return pages_block
