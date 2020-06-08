import pytest
from pages.header_page import HeaderPage
from pages.product_card_page import ProductCardPage
from pages.search_page import SearchPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.full_search_product_page import FullSearchProductPage
from settings.project_setting import TEST_URL, project_page


@pytest.mark.usefixtures('get_driver')
class TestCart:

    @pytest.mark.cart
    def test_cart_in_header_add_from_product_card(self):
        header_cart = HeaderPage(self.driver)
        product_card = ProductCardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        product_card.click_button_buy()
        assert product_card.check_present_button_in_cart()
        assert '1' == header_cart.text_digit_cart_header()
        assert header_cart.text_cart_price().lower() in product_card.text_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_product_card_offers(self):
        header_cart = HeaderPage(self.driver)
        product_card = ProductCardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        prices = product_card.list_text_first_offers_price()
        for i, buy_button in enumerate(product_card.get_first_offers_buy_button()):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 2 == product_card.amount_offers_button_in_cart()
        format_price_for_header_cart = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price_for_header_cart == header_cart.text_cart_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page_recomended(self):
        header_cart = HeaderPage(self.driver)
        search_page = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        prices = search_page.set_tuple_search_recommended_articules_with_price()
        buy_buttons = search_page.get_search_recommended_buttons_buy()
        for i, __ in enumerate(prices):
            buy_buttons[i].click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 3 == search_page.amount_of_search_recommended_buttons_in_cart()
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page(self):
        header_cart = HeaderPage(self.driver)
        search_page = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        prices = search_page.list_text_first_search_block_price()
        for i, buy_button in enumerate(search_page.get_first_search_block_buy_button()):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i + 1))
        assert 3 == search_page.amount_search_block_button_in_cart()
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_catalog(self):
        header_cart = HeaderPage(self.driver)
        catalog_page = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('catalog'))
        catalog_page.click_first_buy_button()
        assert catalog_page.check_present_button_in_cart()
        assert '1' == header_cart.text_digit_cart_header()
        assert header_cart.text_cart_price().lower() in catalog_page.text_first_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_you_watched(self):
        header_cart = HeaderPage(self.driver)
        main_page = MainPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        self.driver.get(TEST_URL)
        main_page.click_first_buy_button_you_watched()
        assert main_page.check_button_in_cart_you_watched()
        assert '1' == header_cart.text_digit_cart_header()
        assert header_cart.text_cart_price().lower() in main_page.text_price_you_watched().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_recomended_in_cart(self):
        header_cart = HeaderPage(self.driver)
        cart_page = CartPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('cart'))
        cart_page.click_first_buy_button_recomended()
        assert cart_page.check_present_button_in_cart_recomended()
        assert '1' == header_cart.text_digit_cart_header()
        assert header_cart.text_cart_price().lower() in cart_page.text_price().lower()

    @pytest.mark.cart
    def test_cart_in_header_add_from_full_search(self):
        header_cart = HeaderPage(self.driver)
        full_search_product_page = FullSearchProductPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('full-search-product'))
        full_search_product_page.click_first_buy_button()
        assert full_search_product_page.check_button_in_cart()
        assert '1' == header_cart.text_digit_cart_header()
        assert header_cart.text_cart_price().lower() in full_search_product_page.text_price().lower()
