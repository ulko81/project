from selenium.webdriver.common.by import By


class TextField:
    base_h1 = By.TAG_NAME, 'h1'
    base_price = By.CSS_SELECTOR, '.catalogue-list .price'
    base_name = By.CSS_SELECTOR, '.catalogue-list strong'
    base_brand = By.CSS_SELECTOR, '.catalogue-list .trademark span'
    base_vendor_code = By.CSS_SELECTOR, '.catalogue-list .trademark'
    base_delivery = By.CSS_SELECTOR, '.catalogue-list .delivery'


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
    search_recommended_name = By.CSS_SELECTOR, '.name-inner p'
    search_recommended_brand = By.CSS_SELECTOR, '.name-inner .name>strong'
    search_recommended_delivery = By.CSS_SELECTOR, '.general-info .delivery'
    search_first_offer_price = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .price'
    search_first_offer_vendor_code = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .name-inner a strong'
    search_first_offer_name = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .name-inner p'
    search_first_offer_brand = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .name-inner .name>strong'
    search_first_offer_delivery = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .general-info .delivery'


class CardTextField:
    card_price = By.CSS_SELECTOR, '.product-short-info .price'
    card_first_offers_price = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .price'
    card_product_brand = By.CSS_SELECTOR, '.short-info-block .bold:first-child'
    card_product_vendor_code = By.CSS_SELECTOR, '.short-info-block .bold:nth-child(2)'
    card_delivery = By.CSS_SELECTOR, '.product-short-info .delivery'
    card_first_offer_name = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) td:nth-child(2)'
    card_first_offer_brand = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name strong'
    card_first_offer_vendor_code = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name a'
    card_first_offer_delivery = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery'
    card_first_offer_delivery_date = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery .bold'
    card_first_offer_delivery_time = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery-time'


class CartTextField:
    cart_name = By.CSS_SELECTOR, '.grid-table .name-inner p'
    cart_brand = By.CSS_SELECTOR, '.grid-table .name>strong'
    cart_vendor_code = By.CSS_SELECTOR, '.grid-table .name a strong'
    cart_delivery_date = By.CSS_SELECTOR, '.grid-table .delivery, .grid-table .exists'
    cart_price = By.CSS_SELECTOR, '.grid-table .price'
    cart_recommended_price = By.CSS_SELECTOR, '.info-block .price'
    cart_recommended_name = By.CSS_SELECTOR, '.info-block .title'
    cart_recommended_brand = By.CSS_SELECTOR, '.info-block .trademark span'
    cart_recommended_vendor_code = By.CSS_SELECTOR, '.info-block .trademark'
    cart_recommended_delivery = By.CSS_SELECTOR, '.info-block .delivery'


class ModuleTextField:
    module_product_name = By.CSS_SELECTOR, '.modal-grid .name-inner p'
    module_product_brand = By.CSS_SELECTOR, '.modal-grid .name>strong'
    module_product_vendor_code = By.CSS_SELECTOR, '.modal-grid .name a strong'
    module_product_delivery = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'
    module_product_price = By.CSS_SELECTOR, '.modal-grid .total'


class MainTextField:
    price = By.CSS_SELECTOR, '.info-block-wrapper .price'
    name = By.CSS_SELECTOR, '.info-block-wrapper .title-wrapper .bold'
    brand = By.CSS_SELECTOR, '.info-block-wrapper .trademark span'
    vendor_code = By.CSS_SELECTOR, '.info-block-wrapper .trademark'
    delivery = By.CSS_SELECTOR, '.info-block-wrapper .delivery'
    title_block = By.CLASS_NAME, 'block-title'
