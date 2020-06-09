from selenium.webdriver.common.by import By


class GeneralLocator:
    h1 = By.TAG_NAME, 'h1'
    h2 = By.TAG_NAME, 'h2'
    h3 = By.TAG_NAME, 'h3'
    button_blue = By.CLASS_NAME, 'btn-blue'
    button_green = By.CLASS_NAME, 'btn-green'
    price = By.CLASS_NAME, 'price'
    phone_field = By.ID, 'phone-field'
    pass_field = By.NAME, 'password'
    delivery_date = By.CSS_SELECTOR, '.delivery span'
    delivery_time = By.CLASS_NAME, 'delivery-time'

