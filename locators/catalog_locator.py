from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class CatalogLocator(BaseLocator):
    seo_our_cities = By.CSS_SELECTOR, 'div[class = "container text-container"]'
