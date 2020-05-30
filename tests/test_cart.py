import pytest
from pages.header_page import HeaderPage
from pages.product_card_page import ProductCardPage
from settings.product_setting import TEST_URL, PRODUCT_CARD_LINK

@pytest.mark.usefixtures('get_driver')
class TestCart:

    @pytest.mark.cart
    def test_check_cart_in_header_add_from_product_card(self):
        header_cart = HeaderPage(self.driver)
        product_card = ProductCardPage(self.driver)
        self.driver.get(TEST_URL + PRODUCT_CARD_LINK)
        product_card.click_button_buy()
        assert product_card.check_present_green_button_buy()
        assert '1' == header_cart.text_digit_cart_header()
        assert product_card.text_card_price().lower() == header_cart.text_cart_header_price().lower()

    def test_cart_in_header_add_from_product_card(self):
        print(['HOME'])
        assert(1==1)

    def test_in_header_add_from_product_card(self):
        assert(2==2)