import pytest
import random
from pages.header_page import HeaderPage
from pages.card_page import CardPage
from pages.search_page import SearchPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.full_search_product_page import FullSearchProductPage
from pages.module_page import ModulePage
from pages.request_by_vin_page import RequestByVinPage
from settings.project_setting import TEST_URL
from settings.project_page import project_page
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestCart(Methods):

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_card(self):
        header_cart = HeaderPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        assert card.check_present_button_in_cart
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in card.text_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_card(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        page_info = card.set_product_info()
        card.click_button_buy()
        card.click_to_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_card_offers(self):
        header_cart = HeaderPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        prices = card.list_text_first_offers_price
        for i, buy_button in enumerate(card.get_first_offers_buy_button):
            buy_button.click()
            assert header_cart.check_text_digit_cart_header(str(i+1))
        assert card.amount_first_offers == card.amount_offers_button_in_cart
        format_price_for_header_cart = str(sum(list(map(lambda el: int(el[:-3]), prices)))) + prices[0][-4:]
        assert format_price_for_header_cart == header_cart.text_cart_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_card_offers(self):
        count = random.randint(0, 1)
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        page_info = card.set_product_info_offers(count)
        card.get_first_offers_buy_button[count].click()
        card.click_offer_in_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
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

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_search_recommended(self):
        count = random.randint(0, 2)
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        search = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        page_info = search.set_recomended_product_info(count)
        search.get_search_recommended_buttons_buy[count].click()
        search.get_search_recommended_buttons_in_cart[0].click()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
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

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_search(self):
        count = random.randint(0, 2)
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        search = SearchPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('search'))
        page_info = search.set_recomended_product_info(count)
        search.get_first_offers_buy_button[count].click()
        search.get_first_offers_in_cart_button[0].click()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_catalog(self):
        header_cart = HeaderPage(self.driver)
        catalog = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('category'))
        catalog.click_first_buy_button()
        assert catalog.check_present_button_in_cart
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in catalog.text_first_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_catalog(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        catalog = CatalogPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('category'))
        page_info = catalog.set_product_info()
        catalog.click_first_buy_button()
        catalog.click_first_in_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_you_watched(self):
        header_cart = HeaderPage(self.driver)
        main = MainPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        self.driver.get(TEST_URL)
        main.click_first_buy_button_you_watched()
        assert main.check_button_in_cart_you_watched
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in main.text_first_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_you_watched(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        main = MainPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        self.driver.get(TEST_URL)
        page_info = main.set_you_watched_product_info()
        main.click_first_buy_button_you_watched()
        main.click_first_in_cart_button_you_watched()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_recommended_in_cart(self):
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('cart'))
        cart.click_first_buy_button_recommended()
        assert cart.check_present_button_in_cart_recommended
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in cart.text_first_recommended_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_recommended_in_cart(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('cart'))
        page_info = cart.set_recommended_product_info()
        cart.click_first_buy_button_recommended()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_in_header_add_from_full_search(self):
        header_cart = HeaderPage(self.driver)
        full_search_product = FullSearchProductPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('full-search-product'))
        full_search_product.click_first_buy_button()
        assert full_search_product.check_button_in_cart
        assert '1' == header_cart.text_digit_cart_header
        assert header_cart.text_cart_price in full_search_product.text_first_price

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_comparison_info_cart_vs_full_search(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        full_search_product = FullSearchProductPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('full-search-product'))
        page_info = full_search_product.set_product_info()
        full_search_product.click_first_buy_button()
        full_search_product.click_first_in_cart_button()
        assert self.driver.current_url == (TEST_URL + project_page.get('cart'))
        cart_info = cart.set_product_info()
        self.close_draggable(self.driver)
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        cart_module_info = module_cart.set_product_info()
        assert page_info == cart_info
        assert page_info == cart_module_info

    @pytest.mark.smoke
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

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_delete_item(self):
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        module_cart = ModulePage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        header_cart.click_cart()
        module_cart.click_to_cart()
        self.close_draggable(self.driver)
        cart.click_button_remove_item()
        assert header_cart.check_cart_without_items

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_module_cart_delete_item(self):
        module_cart = ModulePage(self.driver)
        header_cart = HeaderPage(self.driver)
        card = CardPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        header_cart.click_cart()
        assert module_cart.check_cart_module_info_loaded('грн')
        module_cart.click_button_remove_item()
        assert header_cart.check_cart_without_items

    @pytest.mark.smoke
    @pytest.mark.cart
    @pytest.mark.parametrize('mode', ('sum', 'total'))
    def test_cart_change_count_items(self, mode):
        header_cart = HeaderPage(self.driver)
        cart = CartPage(self.driver)
        card = CardPage(self.driver)
        module_cart = ModulePage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        decrease = card.text_price
        increase = str(int(decrease[:-3]) * 2)
        card.click_button_buy()
        header_cart.click_cart()
        module_cart.click_to_cart()
        self.close_draggable(self.driver)
        cart.click_button_plus()
        assert cart.check_field_digit_field_count('2')
        assert cart.check_sum_price(increase) if mode == 'sum' else cart.check_total_price(increase)
        cart.click_button_minus()
        assert cart.check_field_digit_field_count('1')
        assert cart.check_sum_price(decrease) if mode == 'sum' else cart.check_total_price(decrease)
