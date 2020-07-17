from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class CheckoutLocator(BaseLocator):
    delivery_tooltip = By.CLASS_NAME, 'preloader '
    checkout_user_name = By.CSS_SELECTOR, '.user-title span'
