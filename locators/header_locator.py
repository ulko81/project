from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class HeaderLocator(BaseLocator):
    button_blue = By.CLASS_NAME, 'btn-blue'
    button_green = By.CLASS_NAME, 'btn-green'
    button_white = By.CLASS_NAME, 'btn-white'
    button_darkblue = By.CLASS_NAME, 'btn-darkblue'
    header_language_select = By.CSS_SELECTOR, '.lang-dd-button button'
    cart_header_digit = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_header_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
    mega_menu = By.CLASS_NAME, 'mega-menu-link'
    user_menu = By.CLASS_NAME, 'user-menu-toggler '
    contact = By.CSS_SELECTOR, '.header-contact-nav a'
    logo = By.CSS_SELECTOR, 'svg[name = "logo"] path'
    module_product_name = By.CSS_SELECTOR, '.modal-grid .name-inner p'
    module_product_brand = By.CSS_SELECTOR, '.modal-grid .name>strong'
    module_product_vendor_code = By.CSS_SELECTOR, '.modal-grid .name a strong'
    module_product_delivery = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    module_product_price = By.CSS_SELECTOR, '.modal-grid .total'
    profile_empty = By.CSS_SELECTOR, '.profile button'
    profile_with_auth = By.CSS_SELECTOR, '.profile .colored .user-menu-title'
    cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'
