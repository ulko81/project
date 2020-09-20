from helpers.locators import Locators


class MixinGarage:
    def __init__(self):
        self.locators = Locators
        self.button_car_controls_edit = self.locators.car_controls_edit_button
        self.button_ok_car_vin = self.locators.carVIN_button_ok
        self.button_ok_car_year = self.locators.carYear_button_ok
        self.button_car_delete = self.locators.button_trash
        self.button_car_confirm_delete = self.locators.garage_dd_content_button_blue
        self.car_year = self.locators.car_vin
        self.car_vin = self.locators.car_year
        self.car_name = self.locators.car_name
        self.vin_field = self.locators.carVIN_field
        self.year_field = self.locators.carYear_field
        self.carYear_field = self.locators.carYear_field
