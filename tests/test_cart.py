import pytest
import random
from pages.header import HeaderPage
from pages.card import CardPage
from pages.search import SearchPage
from pages.catalog import CatalogPage
from pages.main import MainPage
from pages.cart import CartPage
from pages.full_search_product import FullSearchProductPage
from pages.request_by_vin import RequestByVinPage
from settings.project_setting import TEST_URL, project_page
from methods.general_method import GeneralMethod


@pytest.mark.usefixtures('get_driver')
class TestCart(GeneralMethod):

    @pytest.mark.cart
    def test_cart_in_header_add_from_card(self):
        header_cart = HeaderPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        card.click_button_buy()
        assert card.check_present_button_in_cart
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in card.text_price

    @pytest.mark.cart
    def test_comparison_info_cart_vs_card(self):
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        page_info = card.set_product_info()
        card.click_button_buy()
        card.click_to_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        header_cart.click_cart_in_header()
        assert header_cart.check_cart_module_info_loaded('грн')
        cart_module_info = header_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.cart
    def test_cart_in_header_add_from_card_offers(self):
        header_cart = HeaderPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        prices = card.list_text_first_offers_price
        for i, buy_button in enumerate(card.get_first_offers_buy_button):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 2 == card.amount_offers_button_in_cart
        format_price_for_header_cart = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price_for_header_cart == header_cart.text_cart_price

    # TO-DO
    @pytest.mark.cart
    def test_comparison_info_cart_vs_card_offers(self):
        count = random.randint(0, 1)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        page_info = card.set_product_info_offers(count)
        card.get_first_offers_buy_button()[count].click()
        card.click_offers_in_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        header_cart.click_cart_in_header()
        assert header_cart.check_cart_module_info_loaded('грн')
        cart_module_info = header_cart.set_product_info()
        # assert page_info == cart_info
        # assert page_info == cart_module_info
        print(page_info)
        print(cart_info)
        print(cart_module_info)

    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page_recommended(self):
        header_cart = HeaderPage(self.driver)
        search = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        prices = search.list_search_recommended_prices
        buy_buttons = search.get_search_recommended_buttons_buy
        for i, __ in enumerate(prices):
            buy_buttons[i].click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert 3 == search.amount_of_search_recommended_buttons_in_cart
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_price

    # TO-DO
    @pytest.mark.cart
    def test_cart_in_header_add_from_search_page(self):
        header_cart = HeaderPage(self.driver)
        search = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        prices = search.list_text_first_search_block_price
        for i, buy_button in enumerate(search.get_first_offers_buy_button):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i + 1))
        assert 3 == search.amount_first_offers_button_in_cart
        format_price = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price == header_cart.text_cart_price

    @pytest.mark.cart
    def test_cart_in_header_add_from_catalog(self):
        header_cart = HeaderPage(self.driver)
        catalog = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('catalog'))
        catalog.click_first_buy_button()
        assert catalog.check_present_button_in_cart
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in catalog.text_first_price

    @pytest.mark.cart
    def test_cart_in_header_add_from_you_watched(self):
        header_cart = HeaderPage(self.driver)
        main = MainPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        self.driver.get(TEST_URL)
        main.click_first_buy_button_you_watched()
        assert main.check_button_in_cart_you_watched()
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in main.text_price_you_watched()

    @pytest.mark.cart
    def test_cart_in_header_add_from_recomended_in_cart(self):
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('cart'))
        cart.click_first_buy_button_recomended()
        assert cart.check_present_button_in_cart_recomended()
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in cart.text_first_price_recomended()

    @pytest.mark.cart
    def test_cart_in_header_add_from_full_search(self):
        header_cart = HeaderPage(self.driver)
        full_search_product_page = FullSearchProductPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('full-search-product'))
        full_search_product_page.click_first_buy_button()
        assert full_search_product_page.check_button_in_cart()
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in full_search_product_page.text_price()

    @pytest.mark.cart
    def test_cart_in_header_add_from_vin_request(self):
        self.driver.get(TEST_URL)
        header_cart = HeaderPage(self.driver)
        header_profile = HeaderPage(self.driver)
        request_by_vin = RequestByVinPage(self.driver)
        self.login(self.driver)
        assert header_profile.check_profile_auth()
        self.driver.get(TEST_URL + project_page.get('request_by_vin'))
        request_by_vin.click_buy_button()
        assert request_by_vin.check_button_in_cart
        assert header_cart.text_digit_cart_header
        assert header_cart.text_cart_price
