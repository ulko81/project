from selenium.webdriver.common.by import By


class Link:
    popular_manufactures = By.CSS_SELECTOR, '.popular-manufactures-container a'
    popular_models = By.CSS_SELECTOR, '.popular-models-block a'
    popular_categories = By.CSS_SELECTOR, '.popular-categories-container a'
