from selenium.webdriver.common.by import By


class TextField:
    base_h1 = By.TAG_NAME, 'h1'
    base_price = By.CLASS_NAME, 'price'


class HeaderTextField:
    cart_header_digit = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'
    cart_header_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'


class FooterTextField:
    pass


class CatalogTextField:
    pass


class SearchTextField:
    search_recommended_price = By.CSS_SELECTOR, '.price-wrapper .price'
    search_recommended_vendor_code = By.CSS_SELECTOR, '.name-inner a strong'
    search_first_offer_price = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .price'


class CardTextField:
    card_price = By.CSS_SELECTOR, '.product-short-info .price'
    card_first_offers_price = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .price'
    card_product_brand = By.CSS_SELECTOR, '.short-info-block .bold:first-child'
    card_product_vendor_code = By.CSS_SELECTOR, '.short-info-block .bold:nth-child(2)'
    card_delivery_date = By.CSS_SELECTOR, '.delivery span'
    card_delivery_time = By.CLASS_NAME, 'delivery-time'
    card_first_offer_name = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) td:nth-child(2)'
    card_first_offer_brand = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name strong'
    card_first_offer_vendor_code = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name a'
    card_first_offer_delivery_date = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery span'
    card_first_offer_delivery_time = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery-time'


class CartTextField:
    cart_recommended_price = By.CSS_SELECTOR, '.info-block .price'
    cart_product_name = By.CSS_SELECTOR, '.grid-table .name-inner p'
    cart_product_brand = By.CSS_SELECTOR, '.grid-table .name>strong'
    cart_product_vendor_code = By.CSS_SELECTOR, '.grid-table .name a strong'
    cart_product_delivery_date = By.CSS_SELECTOR, '.grid-table .delivery, .grid-table .exists'
    cart_product_price = By.CSS_SELECTOR, '.grid-table .price'


class ModuleTextField:
    module_product_name = By.CSS_SELECTOR, '.modal-grid .name-inner p'
    module_product_brand = By.CSS_SELECTOR, '.modal-grid .name>strong'
    module_product_vendor_code = By.CSS_SELECTOR, '.modal-grid .name a strong'
    module_product_delivery = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    module_product_price = By.CSS_SELECTOR, '.modal-grid .total'


class MainTextField:
    pass
