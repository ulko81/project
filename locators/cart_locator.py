from selenium.webdriver.common.by import By


class CartLocator:
    product_name = By.CSS_SELECTOR, '.grid-table .name-inner p'
    product_brand = By.CSS_SELECTOR, '.grid-table .name>strong'
    product_vendor_code = By.CSS_SELECTOR, '.grid-table .name a strong'
    product_delivery = By.CSS_SELECTOR, '.grid-table .delivery'
    #product_total_price = ''


