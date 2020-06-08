from selenium.webdriver.common.by import By


class SearchLocator:
    search_recommended_buttons_buy = By.CSS_SELECTOR, '.price-wrapper .btn-blue'
    search_recommended_buttons_in_cart = By.CSS_SELECTOR, '.price-wrapper .btn-green'
    search_recommended_prices = By.CSS_SELECTOR, '.price-wrapper .price'
    search_recommended_vendor_codes = By.CSS_SELECTOR, '.name-inner a strong'
    first_search_block_buy_button = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .btn-blue'
    search_block_button_in_cart = By.CSS_SELECTOR, '.grid-table .btn-green'
    first_search_block_price = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .price'

