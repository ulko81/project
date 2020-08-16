from pages.base_page import BasePage
from locators.garage_locator import GarageLocator


class GaragePage(BasePage, GarageLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_car(self):
        self.click(self.button_car_controls_edit)

    def fill_vin_field(self, vin):
        self.get_web_element(self.car_vin_field).send_keys(vin)

    def fill_year_field(self, year):
        self.get_web_element(self.car_year_field).send_keys(year)

    def click_button_ok_car_vin(self):
        self.click(self.button_ok_car_vin)

    def click_button_ok_car_year(self):
        self.click(self.button_ok_car_year)

    @property
    def text_car_year(self):
        return self.get_web_element(self.car_year).text

    @property
    def text_car_vin(self):
        return self.get_web_element(self.car_vin).text

    def click_delete_car(self):
        self.click(self.button_car_delete)

    def click_confirm_delete_car(self):
        self.click(self.button_car_confirm_delete)

    @property
    def text_car_name(self):
        return self.get_web_element(self.car_name).text

