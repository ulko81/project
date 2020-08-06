from pages.header_page import HeaderPage
from pages.base_page import BasePage
from locators.base_locator import BaseLocator
from helpers.dict_helper import *
from selenium.webdriver.common.keys import Keys
import random


class GeneralMethod:


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

    @staticmethod
    def clear_field(driver, locator):
        field = BasePage(driver)
        return field.get_web_element(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)