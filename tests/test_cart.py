import pytest
from pages.header_page import HeaderPage
from pages.product_card_page import ProductCardPage
from pages.search_page import SearchPage
from pages.catalog_page import CatalogPage
from settings.product_setting import TEST_URL, product_links


@pytest.mark.usefixtures('get_driver')
class TestCart:

    @pytest.mark.cart
    def test_check_cart_in_header_add_from_product_card(self):
        header_cart = HeaderPage(self.driver)
        product_card = ProductCardPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('product_card_page'))
        product_card.click_button_buy()
        assert product_card.check_present_green_button_buy()
        assert '1' == header_cart.text_digit_cart_header()
        assert product_card.text_card_price().lower() == header_cart.text_cart_header_price().lower()

    @pytest.mark.cart
    def test_check_cart_in_header_add_from_product_card_offers(self):
        header_cart = HeaderPage(self.driver)
        product_card = ProductCardPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('product_card_page'))
        prices = product_card.list_text_first_offers_price()
        for i, buy_button in enumerate(product_card.get_first_offers_buy_blue_button()):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 2 == product_card.amount_offers_green_button_buy()
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_header_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page_recomended(self):
        header_cart = HeaderPage(self.driver)
        search_page = SearchPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('search_page'))
        prices = search_page.set_tuple_search_recommended_articules_with_price()
        buy_buttons = search_page.get_search_recommended_buttons_buy_blue()
        for i, __ in enumerate(prices):
            buy_buttons[i].click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 3 == search_page.get_amount_of_search_recommended_buttons_buy_green()
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_header_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page(self):
        header_cart = HeaderPage(self.driver)
        search_page = SearchPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('search_page'))
        prices = search_page.set_tuple_search_recommended_articules_with_price()
        buy_buttons = search_page.get_search_recommended_buttons_buy_blue()
        for i, __ in enumerate(prices):
            buy_buttons[i].click()
            assert header_cart.check_text_digit_cart_header(str(i + 1))
        assert 3 == search_page.get_amount_of_search_recommended_buttons_buy_green()
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_header_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_catalog(self):
        header_cart = HeaderPage(self.driver)
        catalog_page = CatalogPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('catalog'))
        catalog_page.click_first_buy_button()
        assert catalog_page.check_present_green_button_buy()
        assert '1' == header_cart.text_digit_cart_header()
        assert catalog_page.text_first_price().lower() == header_cart.text_cart_header_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_catalog(self):
        header_cart = HeaderPage(self.driver)
        catalog_page = CatalogPage(self.driver)
        self.driver.get(TEST_URL + product_links.get('catalog'))
        catalog_page.click_first_buy_button()
        assert catalog_page.check_present_green_button_buy()
        assert '1' == header_cart.text_digit_cart_header()
        assert catalog_page.text_first_price().lower() == header_cart.text_cart_header_price().lower()
    