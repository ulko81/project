from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class GarageLocator(BaseLocator):
    car_year = By.CLASS_NAME, 'car-year'
    car_vin = By.CLASS_NAME, 'car-vin'
