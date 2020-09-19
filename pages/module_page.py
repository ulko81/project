from pages.base_page import BasePage
from mixins.mixin_module import MixinModule


class ModulePage(BasePage, MixinModule):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinModule.__init__(self)

    @property
    def text_languages_module(self):
        return ' '.join(tuple(map(lambda el: el.text, self.get_web_elements(self.button_language_select))))

    def click_module_button_order(self):
        self.click(self.order)

    def click_car_year_selected(self, year):
        item = f'{self.list_years[0]}', f'{self.list_years[1].format(year)}'
        self.click(item)

    def fill_manufacture_field(self, manufacture):
        self.get_web_element(self.input_manufacture).send_keys(manufacture)

    def click_car_manufacture_selected(self):
        self.click(self.list_manufactures)

    def click_car_model_selected(self, model):
        item = f'{self.list_models[0]}', f'{self.list_models[1].format(model)}'
        self.click(item)

    def click_car_type_model_selected(self, type_model):
        item = f'{self.list_type_models[0]}', f'{self.list_type_models[1].format(type_model)}'
        self.click(item)

    def click_car_modification_selected(self, modification):
        item = f'{self.list_modification[0]}', f'{self.list_modification[1].format(modification)}'
        self.click(item)

    def click_years_select(self, mode):
        self.click(self.my_car_years) if mode == 'my_car'else self.click(self.parts_search_years)

    def click_munufactures_select(self, mode):
        self.click(self.my_car_manufactures) if mode == 'my_car' else self.click(self.parts_search_manufactures)

    def click_models_select(self, mode):
        self.click(self.my_car_models) if mode == 'my_car' else self.click(self.parts_search_models)

    def click_type_models_select(self, mode):
        self.click(self.my_car_type_models) if mode == 'my-car' else self.click(self.parts_search_type_models)

    def click_modifications_select(self, mode):
        self.click(self.my_car_modifications) if mode == 'my-car' else self.click(self.parts_search_modifications)

    def click_select_car(self):
        self.click(self.btn_icon)

    def click_edit_car(self):
        self.click(self.button_car_controls_edit)

    def fill_vin_field(self, vin):
        self.get_web_element(self.carVIN_field).send_keys(vin)

    def fill_year_field(self, year):
        self.get_web_element(self.carYear_field).send_keys(year)

    def click_button_ok_car_vin(self):
        self.click(self.carVIN_button_ok)

    def click_button_ok_car_year(self):
        self.click(self.carYear_button_ok)

    def text_car_vin(self, mode):
        if mode == 'my_cars':
            return self.get_web_element(self.my_cars_vin).text
        else:
            return self.get_web_element(self.chosen_car_vin).text

    @property
    def text_price(self):
        return self.get_web_element(self.price).text

    def check_cart_module_info_loaded(self, text):
        return self.text_present_in_element(self.price, text)

    @property
    def text_name(self):
        return self.get_web_element(self.name).text

    @property
    def text_brand(self):
        return self.get_web_element(self.brand).text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.vendor_code).text

    @property
    def text_delivery(self):
        return CartMethod.change_format_date_cart(self.get_web_element(self.delivery).text).lower()

    def set_product_info(self):
        return {self.text_price, self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery}

    def fill_module_phone_field(self, phone):
        self.get_web_element(self.phone_field).send_keys(phone)

    def fill_module_pass_field(self, password):
        self.get_web_element(self.password_field).send_keys(password)

    def click_module_enter(self):
        self.click(self.button_blue)

    def click_delete_car(self):
        self.click(self.button_car_delete)

    def click_confirm_delete_car(self):
        self.click(self.button_confirm_delete)

    def click_button_go_to_garage(self):
        self.click(self.my_cars_button_go_to_garage)

    @property
    def set_text_car_name(self):
        return set(map(lambda el: el.text, self.get_web_elements(self.car_name)))

    def click_to_cart(self):
        self.click(self.button_to_cart)

    def click_button_remove_item(self):
        self.click(self.cart_remove_item)

    def clear_year(self):
        self.clear_year_field(self.driver, self.carYear_field)


