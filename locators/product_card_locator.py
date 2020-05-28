from selenium.webdriver.common.by import By


class ProductCardLocator:
    button_buy_blue = (By.CSS_SELECTOR, '.list-item-btns .btn-blue')
    button_buy_green = (By.CSS_SELECTOR, '.list-item-btns .btn-green')
    card_price = (By.CSS_SELECTOR, '.product-short-info .price')