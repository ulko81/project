from methods.general_method import GeneralMethod
from pages.module_page import ModulePage
from pages.header_page import HeaderPage
from locators.module_locator import ModuleLocator


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
    def change_year_vin(driver, **car_attr):
        edit_car = ModulePage(driver)
        if car_attr.get('year'):
            edit_car.click_edit_car()
            GeneralMethod.clear_field(driver, ModuleLocator.my_car_chosen_car_field_year)
            edit_car.fill_year_field(car_attr.get('year'))
            edit_car.click_chosen_car_button_ok_year()
        if car_attr.get('vin'):
            edit_car.fill_vin_field(car_attr.get('vin'))
            edit_car.click_chosen_car_button_ok_vin()

    @staticmethod
    def delete_chosen_car(driver):
        delete_car = ModulePage(driver)
        delete_car.click_delete_car()
        delete_car.click_confirm_delete_car()
