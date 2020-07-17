from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class CartLocator(BaseLocator):
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
