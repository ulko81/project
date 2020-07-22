import os
from pages.header_page import HeaderPage
from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage
from locators.base_locator import BaseLocator
from helpers.dict_helper import *
import random


class GeneralMethod:

    @property
    def get_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import user_login
            return user_login

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
        header.click_empty_profile()
        header.fill_module_phone_field(login)
        header.fill_module_pass_field(password)
        header.click_module_enter()

    def login_checkout(self, driver, login=None, password=None):
        if not login:
            login = self.get_username
            password = self.get_password
        checkout = CheckoutPage(driver)
        checkout.fill_checkout_phone_field(login)
        checkout.fill_checkout_pass_field(password)
        checkout.click_checkout_enter()

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
            preloader.get_visible_element(BaseLocator.icon_preload)
        except Exception:
            pass
        preloader.check_invisible_element(BaseLocator.icon_preload)

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

