from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class MainLocator(BaseLocator):
    price = By.CSS_SELECTOR, '.info-block-wrapper .price'
    name = By.CSS_SELECTOR, '.info-block-wrapper .title-wrapper .bold'
    brand = By.CSS_SELECTOR, '.info-block-wrapper .trademark span'
    vendor_code = By.CSS_SELECTOR, '.info-block-wrapper .trademark'
    delivery = By.CSS_SELECTOR, '.info-block-wrapper .delivery'
    title_block = By.CLASS_NAME, 'block-title'
