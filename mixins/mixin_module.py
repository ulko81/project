from helpers.locators import Locators
from helpers.methods import Methods


class MixinModule:
    def __init__(self):
        self.locators = Locators()
        self.methods = Methods()
        self.button_language_select = self.locators.lang_select_button
        self.order = self.locators.button_checkout
        self.list_years = self.locators.car_year_block_button
        self.input_manufacture = self.locators.car_manufacture_block_input
        self.list_manufactures = self.locators.manufacture_list_button
        self.list_models = self.locators.car_model_wrapper_button
        self.list_type_models = self.locators.car_model_type_block_button
        self.list_modification = self.locators.car_modification_block_tr
        self.my_car_years = self.locators.add_car_block_years
        self.parts_search_years = self.locators.garage_add_car_years
        self.my_car_manufactures = self.locators.add_car_block_manufactures
        self.parts_search_manufactures = self.locators.garage_add_car_manufactures
        self.my_car_models = self.locators.add_car_block_models
        self.parts_search_models = self.locators.garage_add_car_models
        self.my_car_type_models = self.locators.add_car_block_type_models
        self.parts_search_type_models = self.locators.garage_add_car_type_models
        self.my_car_modifications = self.locators.add_car_block_modifications
        self.parts_search_modifications = self.locators.garage_add_car_modifications
        self.btn_icon = self.locators.btn_icon
        self.button_car_controls_edit = self.locators.button_car_controls_edit
        self.carVIN_field = self.locators.carVIN_field
        self.carYear_field = self.locators.carYear_field
        self.carVIN_button_ok = self.locators.carVIN_button_ok
        self.carYear_button_ok = self.locators.carYear_button_ok
        self.my_cars_vin = self.locators.garage_car_list_vin
        self.chosen_car_vin = self.locators.chosen_car_info_vin
        self.price = self.locators.modal_grid_price
        self.name = self.locators.modal_grid_name
        self.brand = self.locators.modal_grid_brand
        self.vendor_code = self.locators.modal_grid_vendor_code
        self.delivery = self.locators.modal_grid_delivery
        self.phone_field = self.locators.phone_field
        self.password_field = self.locators.password_field
        self.button_blue = self.locators.btn_blue
        self.button_car_delete = self.locators.button_trash
        self.button_confirm_delete = self.locators.garage_dd_content_button_blue
        self.my_cars_button_go_to_garage = self.locators.garage_car_list_a
        self.car_name =self.locators.car_name
        self.button_to_cart = self.locators.button_to_cart
        self.cart_remove_item = self.locators.cart_remove
        self.clear_year_field = self.methods.clear_field