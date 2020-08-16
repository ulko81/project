from methods.general_method import GeneralMethod
from pages.module_page import ModulePage
from pages.header_page import HeaderPage
from locators.base_locator import BaseLocator
from pages.garage_page import GaragePage


class CarMethod:

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
            GeneralMethod.clear_field(driver, BaseLocator.car_year_field)
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
