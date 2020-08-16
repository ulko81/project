from selenium.webdriver.common.by import By


class BaseLocator:
    button_blue = By.CLASS_NAME, 'btn-blue'
    button_green = By.CLASS_NAME, 'btn-green'
    button_white = By.CLASS_NAME, 'btn-white'
    button_darkblue = By.CLASS_NAME, 'btn-darkblue'
    icon_preload = By.CSS_SELECTOR, '.preloader.visible'
    phone_field = By.ID, 'phone-field'
    pass_field = By.NAME, 'password'
    multi_user_block = By.CSS_SELECTOR, '.user-change-counterparty button'
    popular_manufactures = By.CSS_SELECTOR, '.popular-manufactures-container a'
    popular_models = By.CSS_SELECTOR, '.popular-models-block a'
    popular_categories = By.CSS_SELECTOR, '.popular-categories-container a'
    base_h1 = By.TAG_NAME, 'h1'
    cars_block_title = By.CSS_SELECTOR, '.car-descendants-wrapper h2'
    cars_block = By.CSS_SELECTOR, '.car-descendants-wrapper a'
    base_price = By.CSS_SELECTOR, '.catalogue-list .price'
    base_name = By.CSS_SELECTOR, '.catalogue-list strong'
    base_brand = By.CSS_SELECTOR, '.catalogue-list .trademark span'
    base_vendor_code = By.CSS_SELECTOR, '.catalogue-list .trademark'
    base_delivery = By.CSS_SELECTOR, '.catalogue-list .delivery'
    base_description = By.CSS_SELECTOR, 'meta[name = "description"]'
    you_watched_button_blue = By.CSS_SELECTOR, '.info-block-wrapper .btn-blue'
    you_watched_button_green = By.CSS_SELECTOR, '.info-block-wrapper .btn-green'
    breadcrumbs = By.CSS_SELECTOR, '.breadcrumbs a'
    breadcrumbs_last_el = By.CLASS_NAME, 'breadcrumbs-current-path'
    breadcrumbs_devider = By.CLASS_NAME, 'breadcrumbs-divider'
    btn_icon = By.CLASS_NAME, 'btn-icon'
    button_car_controls_edit = By.CSS_SELECTOR, 'button[class="car-controls-edit"]'
    car_vin_field = By.CSS_SELECTOR, 'input[aria-label = "carVIN"]'
    car_year_field = By.CSS_SELECTOR, 'input[aria-label = "carYear"]'
    car_name = By.CLASS_NAME, 'car-name'
    button_ok_car_vin = By.CSS_SELECTOR, 'input[aria-label = "carVIN"]~button'
    button_ok_car_year = By.CSS_SELECTOR, 'input[aria-label = "carYear"]~button'
    button_car_delete = By.XPATH, '//*[@name="trash"]/../..'
    button_car_confirm_delete = By.CSS_SELECTOR, '.garage-dd-content .btn-blue'

