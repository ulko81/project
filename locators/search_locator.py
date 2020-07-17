from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class SearchLocator(BaseLocator):
    search_recommended_button_blue = By.CSS_SELECTOR, '.price-wrapper .btn-blue'
    search_recommended_button_green = By.CSS_SELECTOR, '.price-wrapper .btn-green'
    search_first_offer_button_blue = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .btn-blue'
    search_first_offer_button_green = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .btn-green'
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
