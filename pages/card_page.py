from pages.base_page import BasePage
from locators.card_locator import CardLocator


class CardPage(BasePage, CardLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_buy(self):
        self.click(self.card_button_blue)

    def click_to_cart_button(self):
        self.click(self.card_button_green)

    @property
    def check_present_button_in_cart(self):
        return self.get_web_element(self.card_button_green)

    @property
    def text_price(self):
        return self.get_web_element(self.card_price).text.lower()

    @property
    def get_first_offers_buy_button(self):
        return self.get_web_elements(self.card_first_offer_button_blue)

    def click_offer_in_cart_button(self):
        return self.click(self.button_green)

    @property
    def amount_offers_button_in_cart(self):
        return self.amount_of_elements(self.button_green)

    @property
    def list_text_first_offers_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.card_first_offers_price)))

    def text_first_offers_price(self, order):
        return self.get_web_elements(self.card_first_offers_price)[order].text

    @property
    def text_name(self):
        name = self.get_web_element(self.base_h1).text
        return name[:name.find('(')-1]

    def text_first_offers_name(self, order):
        return self.get_web_elements(self.card_first_offer_name)[order].text

    @property
    def text_brand(self):
        return self.get_web_element(self.card_product_brand).text

    def text_first_offers_brand(self, order):
        return self.get_web_elements(self.card_first_offer_brand)[order].text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.card_product_vendor_code).text

    def text_first_offers_vendor_code(self, order):
        return self.get_web_elements(self.card_first_offer_vendor_code)[order].text

    @property
    def text_delivery(self):
        return self.get_web_element(self.card_delivery).text.lower()

    def text_first_offers_delivery(self, order):
        return self.get_web_elements(self.card_first_offer_delivery)[order].text.lower()

    def set_product_info(self):
        return {self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery, self.text_price}

    def set_product_info_offers(self, order):
        return {self.text_first_offers_name(order), self.text_first_offers_brand(order),
                self.text_first_offers_vendor_code(order), self.text_first_offers_delivery(order),
                self.text_first_offers_price(order)}
