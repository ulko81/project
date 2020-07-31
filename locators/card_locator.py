from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class CardLocator(BaseLocator):
    card_button_blue = By.CSS_SELECTOR, '.list-item-btns .btn-blue'
    card_button_green = By.CSS_SELECTOR, '.list-item-btns .btn-green'
    first_offers = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1)'
    card_first_offer_button_blue = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-blue'
    card_first_offer_button_green = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-green'
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
    card_product_attributes_values = By.CSS_SELECTOR, '.product-attributes a'
