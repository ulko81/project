from selenium.webdriver.common.by import By


class HeaderLocator:
    digit_cart_header = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_header_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
