from selenium.webdriver.common.by import By


class HeaderLocator:
    digit_cart_header = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_header_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
    profile_empty = By.CSS_SELECTOR, '.profile button'
    cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'
    cart_delivery_info_modal = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    cart_module_price = By.CLASS_NAME, 'quantity-price'
    button_menu_cart_order = By.CSS_SELECTOR, 'a[href = "/checkout/"]'
    button_menu_in_cart = By.CSS_SELECTOR, '.buttons a[href = "/cart/"]'

