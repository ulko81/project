from pages.base_page import BasePage
from locators.cart_locator import CartLocator


class RegistrationPage(BasePage, CartLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def text_cart_price_menu(self, driver):
        return self.get_web_element(driver, self.field_cart_price_menu).text.lower()

    def text_cart_module_price(self, driver):
        return self.check_text_present_in_element(driver, self.field_cart_module_price, "грн").text[4:].lower()

    def text_cart_price(self, driver):
        return self.get_web_element(driver, self.field_cart_price_menu).text.lower()

    def text_fields_sum_price(self, driver):
        return self.get_web_element(driver, self.fields_sum_price).text[7:]

    def click_menu_cart_with_items(self, driver):
        return self.click(driver, self.button_menu_cart_with_items)

    def click_menu_cart_without_items(self, driver):
        return self.click(driver, self.button_menu_cart_without_items)

    def click_menu_cart_order(self, driver):
        return self.click(driver, self.button_menu_cart_order)

    def click_menu_to_cart(self, driver):
        return self.click(driver, self.button_menu_in_cart)

    def text_count_in_icon_cart(self, driver):
        return self.get_web_element(driver, self.cart_count).text

    def set_text_products_in_cart(self, driver):
        return set(map(lambda element: element.text, self.get_web_elements(driver, self.field_cart_product)))

    def check_text_in_icon_cart(self, driver, text):
        self.check_text_present_in_element(driver, self.cart_count, text)

    def click_first_buy_button_in_recomended_products(self, driver):
        self.get_visible_elements(driver, self.button_blue)[0].click()

    def check_visible_buy_green_button_in_recomended_products(self, driver):
        return self.get_web_element(driver, self.button_green)

    def text_product_in_cart(self, driver):
        return self.get_web_element(driver, self.field_cart_product).text

    def set_text_cart_product_info(self, driver):
        return set(self.get_web_element(driver, self.cart_product_info).text.replace('\n', ' ').split(' '))

    def text_cart_delivery_info_modal(self, driver):
        return self.get_web_element(driver, self.cart_delivery_info_modal).text.replace('\n', ' ').lower()

    def text_cart_delivery_info(self, driver):
        return self.get_web_element(driver, self.cart_delivery_info).text.replace('\n', ' ').lower()

    def text_first_price_in_recomended_products(self, driver):
        return self.get_web_elements(driver, self.field_price_price_block)[0].text

    def set_text_product_info_in_recomended_products(self, driver):
        tm_art = self.get_web_elements(driver, self.title_wrapper_trademark)[0].text
        name = self.get_web_elements(driver, self.title_wrapper)[0].get_attribute("title")
        return set(("{} {}".format(tm_art, name)).replace('\n', ' ').split(' '))
