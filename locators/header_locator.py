from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class HeaderLocator(BaseLocator):
    header_language_select = By.CSS_SELECTOR, '.lang-dd-button button'
    cart_header_digit = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_header_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
    mega_menu = By.CLASS_NAME, 'mega-menu-link'
    user_menu = By.CLASS_NAME, 'user-menu-toggler '
    contact = By.CSS_SELECTOR, '.header-contact-nav a'
    logo = By.CSS_SELECTOR, 'svg[name = "logo"] path'
    profile_empty = By.CSS_SELECTOR, '.profile button'
    profile_with_auth = By.CSS_SELECTOR, '.profile .colored .user-menu-title'
    cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'
    my_car_empty = By.CLASS_NAME, 'garage'
    my_car_with_car = By.CSS_SELECTOR, '.garage  div[title = "Выбранный автомобиль"]'
