from pages.base_page import BasePage
from locators.module_locator import ModuleLocator
from methods.cart_method import CartMethod


class ModulePage(BasePage, ModuleLocator):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def text_languages_module(self):
        return ' '.join(tuple(map(lambda el: el.text, self.get_web_elements(self.button_language_select))))

    def click_module_button_order(self):
        self.click(self.cart_button_cart_order)

    def click_car_year_selected(self, year):
        item = '{}'.format(self.list_car_years[0]), '{}'.format(self.list_car_years[1].format(year))
        self.click(item)

    def fill_manufacture_field(self, manufacture):
        self.get_web_element(self.car_input_manufacture).send_keys(manufacture)

    def click_car_manufacture_selected(self):
        self.click(self.list_car_manufactures)

    def click_car_model_selected(self, model):
        item = '{}'.format(self.list_car_models[0]), '{}'.format(self.list_car_models[1].format(model))
        self.click(item)

    def click_car_type_model_selected(self, type_model):
        item = '{}'.format(self.list_car_type_models[0]), '{}'.format(self.list_car_type_models[1].format(type_model))
        self.click(item)

    def click_car_modification_selected(self, modification):
        item = '{}'.format(self.list_car_modification[0]), '{}'.format(self.list_car_modification[1]
                                                                       .format(modification))
        self.click(item)

    def click_years_select(self, mode):
        self.click(self.my_car_years_select) if mode == 'my_car'else self.click(self.parts_search_years_select)

    def click_munufactures_select(self, mode):
        if mode == 'my_car':
            self.click(self.my_car_manufactures_select)
        else:
            self.click(self.parts_search_manufactures_select)

    def click_models_select(self, mode):
        self.click(self.my_car_models_select) if mode == 'my_car' else self.click(self.parts_search_models_select)

    def click_type_models_select(self, mode):
        if mode == 'my-car':
            self.click(self.my_car_type_models_select)
        else:
            self.click(self.parts_search_type_models_select)

    def click_modifications_select(self, mode):
        if mode == 'my-car':
            self.click(self.my_car_modifications_select)
        else:
            self.click(self.parts_search_modifications_select)

    def click_select_car(self):
        self.click(self.btn_icon)

    def click_edit_car(self):
        self.click(self.my_car_chosen_car_button_edit)

    def fill_vin_field(self, vin):
        self.get_web_element(self.my_car_chosen_car_field_vin).send_keys(vin)

    def fill_year_field(self, year):
        self.get_web_element(self.my_car_chosen_car_field_year).send_keys(year)

    def click_chosen_car_button_ok_vin(self):
        self.click(self.my_car_chosen_car_button_ok_vin)

    def click_chosen_car_button_ok_year(self):
        self.click(self.my_car_chosen_car_button_ok_year)

    def car_vin(self, mode):
        if mode == 'my_cars':
            return self.get_web_element(self.my_car_my_cars_vin).text
        else:
            return self.get_web_element(self.my_car_chosen_car_vin).text

    @property
    def text_price(self):
        return self.get_web_element(self.cart_product_price).text

    def check_cart_module_info_loaded(self, text):
        return self.text_present_in_element(self.cart_product_price, text)

    @property
    def text_name(self):
        return self.get_web_element(self.cart_product_name).text

    @property
    def text_brand(self):
        return self.get_web_element(self.cart_product_brand).text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.cart_product_vendor_code).text

    @property
    def text_delivery(self):
        return CartMethod.change_format_date_cart(self.get_web_element(self.cart_product_delivery).text).lower()

    def set_product_info(self):
        return {self.text_price, self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery}

    def fill_module_phone_field(self, phone):
        self.get_web_element(self.phone_field).send_keys(phone)

    def fill_module_pass_field(self, password):
        self.get_web_element(self.pass_field).send_keys(password)

    def click_module_enter(self):
        self.click(self.button_blue)

    def click_delete_car(self):
        self.click(self.my_car_chosen_car_button_delete)

    def click_confirm_delete_car(self):
        self.click(self.my_car_confirm_delete)

    def click_button_go_to_garage(self):
        self.click(self.my_car_my_cars_button_go_to_garage)
