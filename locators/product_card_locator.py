from selenium.webdriver.common.by import By


class ProductCardLocator:
    button_buy_blue = By.CSS_SELECTOR, '.list-item-btns .btn-blue'
    button_buy_green = By.CSS_SELECTOR, '.list-item-btns .btn-green'
    card_price = By.CSS_SELECTOR, '.product-short-info .price'
    first_offers_buy_button = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-blue'
    first_offers_price = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .price'
    product_brand = By.CSS_SELECTOR, '.short-info-block .bold:first-child'
    product_vendor_code = By.CSS_SELECTOR, '.short-info-block .bold:nth-child(2)'
