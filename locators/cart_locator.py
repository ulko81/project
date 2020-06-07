from selenium.webdriver.common.by import By


class CartLocator:
    button_menu_cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    button_menu_cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'
    button_menu_cart_order = By.CSS_SELECTOR, 'a[href = "/checkout/"]'
    button_menu_in_cart = By.CSS_SELECTOR, '.buttons a[href = "/cart/"]'
    field_cart_price_menu = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
    field_cart_module_price = By.CLASS_NAME, 'quantity-price'
    field_cart_price = By.CSS_SELECTOR, '.cell-inner .price'
    fields_sum_price = By.CSS_SELECTOR, '.total-wrapper .total'
    field_cart_product = By.CSS_SELECTOR, '.modal-grid .name a strong'
    cart_count = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_product_info = By.CLASS_NAME, 'name-inner'
    cart_delivery_info_modal = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    cart_delivery_info = By.CSS_SELECTOR, '.grid-table .delivery, .grid-table .exists'
