from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class MainLocator(BaseLocator):
    price = By.CSS_SELECTOR, '.info-block-wrapper .price'
    name = By.CSS_SELECTOR, '.info-block-wrapper .title-wrapper .bold'
    brand = By.CSS_SELECTOR, '.info-block-wrapper .trademark span'
    vendor_code = By.CSS_SELECTOR, '.info-block-wrapper .trademark'
    delivery = By.CSS_SELECTOR, '.info-block-wrapper .delivery'
    title_block = By.CLASS_NAME, 'block-title'
    seo_text = By.CLASS_NAME, 'seo-text'
    guide_tabs = By.CSS_SELECTOR, '.guide-tabs .react-tabs__tab-list li'
    guide_tab_selected = By.CSS_SELECTOR, '.guide-tabs li[aria-selected = "true"]'
