from selenium.webdriver.common.by import By


class Button:
    button_blue = By.CLASS_NAME, 'btn-blue'
    button_green = By.CLASS_NAME, 'btn-green'
    button_white = By.CLASS_NAME, 'btn-white'
    button_darkblue = By.CLASS_NAME, 'btn-darkblue'


class HeaderButton:
    profile_empty = By.CSS_SELECTOR, '.profile button'
    profile_with_auth = By.CSS_SELECTOR, '.profile .colored'
    cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'


class FooterButton:
    pass


class CatalogButton:
    pass


class SearchButton:
    search_recommended_button_blue = By.CSS_SELECTOR, '.price-wrapper .btn-blue'
    search_recommended_button_green = By.CSS_SELECTOR, '.price-wrapper .btn-green'
    search_first_offer_button_blue = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .btn-blue'
    search_first_offer_button_green = By.CSS_SELECTOR, '.grid-table .nested-row-0:nth-child(1) .btn-green'


class CardButton:
    card_button_blue = By.CSS_SELECTOR, '.list-item-btns .btn-blue'
    card_button_green = By.CSS_SELECTOR, '.list-item-btns .btn-green'
    card_first_offer_button_blue = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-blue'
    card_first_offer_button_green = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-green'


class CartButton:
    pass


class ModuleButton:
    module_button_cart_order = By.CSS_SELECTOR, 'a[href = "/checkout/"]'
    module_button_to_cart = By.CSS_SELECTOR, '.buttons a[href = "/cart/"]'


class MainButton:
    you_watched_button_blue = By.CSS_SELECTOR, '.info-block-wrapper .btn-blue'
    you_watched_button_green = By.CSS_SELECTOR, '.info-block-wrapper .btn-green'
