from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class ModuleLocator(BaseLocator):
    button_language_select = By.CSS_SELECTOR, '.lang-select button'
    cart_button_cart_order = By.CSS_SELECTOR, 'a[href = "/checkout/"]'
    cart_button_to_cart = By.CSS_SELECTOR, '.buttons a[href = "/cart/"]'
    my_car_years_select = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(1)'
    my_car_manufactures_select = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(2)'
    my_car_models_select = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(3)'
    my_car_type_models_select = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(4)'
    my_car_modifications_select = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(5)'
    parts_search_years_select = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(1)'
    parts_search_manufactures_select = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(2)'
    parts_search_models_select = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(3)'
    parts_search_type_models_select = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(4)'
    parts_search_modifications_select = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(5)'
    cart_product_name = By.CSS_SELECTOR, '.modal-grid .name-inner p'
    cart_product_brand = By.CSS_SELECTOR, '.modal-grid .name>strong'
    cart_product_vendor_code = By.CSS_SELECTOR, '.modal-grid .name a strong'
    cart_product_delivery = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    cart_product_price = By.CSS_SELECTOR, '.modal-grid .total'
    list_car_years = By.CSS_SELECTOR, '.car-year-block button[name = "{}"]'
    list_car_manufactures = By.CSS_SELECTOR, '.manufacture-list button'
    list_car_models = By.CSS_SELECTOR, '.car-model-wrapper button[name = "{}"]'
    list_car_type_models = By.CSS_SELECTOR, '.car-model-type-block button[name = "{}"]'
    list_car_modification = By.CSS_SELECTOR, '.car-modification-block tr[data-name = "{}"]'
    car_input_manufacture = By.CSS_SELECTOR, '.car-manufacture-block input'
    my_car_my_cars_vin = By.XPATH, '//div[@class = "garage-car-list"]//li/div[contains(text(), "VIN")]'
    my_car_chosen_car_vin = By.XPATH, '//div[@class = "chosen-car-info"]//div[contains(text(), "VIN")]'
    my_car_my_cars_button_go_to_garage = By.CSS_SELECTOR, '.garage-car-list a'

