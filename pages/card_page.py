from pages.base_page import BasePage
from mixins.mixin_card import MixinCard


class CardPage(BasePage, MixinCard):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        MixinCard.__init__(self)

    def click_button_buy(self):
        self.click(self.button_blue)

    def click_to_cart_button(self):
        self.click(self.button_green)

    @property
    def check_present_button_in_cart(self):
        return self.get_web_element(self.button_green)

    @property
    def text_price(self):
        return self.get_web_element(self.price).text.lower()

    @property
    def get_first_offers_buy_button(self):
        return self.get_web_elements(self.first_offer_button_blue)

    def click_offer_in_cart_button(self):
        return self.click(self.button_green)

    @property
    def amount_offers_button_in_cart(self):
        return self.amount_of_elements(self.button_green)

    @property
    def list_text_first_offers_price(self):
        return list(map(lambda el: el.text, self.get_web_elements(self.first_offer_price)))

    def text_first_offers_price(self, order):
        return self.get_web_elements(self.first_offer_price)[order].text

    @property
    def text_name(self):
        name = self.get_web_element(self.tag_h1).text
        return name[:name.find('(')-1]

    def text_first_offers_name(self, order):
        return self.get_web_elements(self.first_offer_name)[order].text

    @property
    def text_brand(self):
        return self.get_web_element(self.brand).text

    def text_first_offers_brand(self, order):
        return self.get_web_elements(self.first_offer_brand)[order].text

    @property
    def text_vendor_code(self):
        return self.get_web_element(self.vendor_code).text

    def text_first_offers_vendor_code(self, order):
        return self.get_web_elements(self.first_offer_vendor_code)[order].text

    @property
    def text_delivery(self):
        return self.get_web_element(self.delivery).text.lower()

    def text_first_offers_delivery(self, order):
        return self.get_web_elements(self.first_offer_delivery)[order].text.lower()

    def set_product_info(self):
        return {self.text_name, self.text_brand, self.text_vendor_code, self.text_delivery, self.text_price}

    def set_product_info_offers(self, order):
        return {self.text_first_offers_name(order), self.text_first_offers_brand(order),
                self.text_first_offers_vendor_code(order), self.text_first_offers_delivery(order),
                self.text_first_offers_price(order)}

    @property
    def get_link_first_attribute_value(self):
        return self.get_web_elements(self.product_attributes_values)[0].get_attribute('href')

    def click_first_attribute_value(self):
        self.get_web_elements(self.product_attributes_values)[0].click()

    @property
    def amount_first_offers(self):
        return self.amount_of_elements(self.first_offers)
