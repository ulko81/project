import pytest
from pages.header_page import HeaderPage
from pages.checkout_page import CheckoutPage
from pages.card_page import CardPage
from pages.module_page import ModulePage
from settings.project_setting import TEST_URL, test_user
from helpers.project_page import project_page
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestAuthorization(Methods):

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_simple(self):
        """Test 1"""
        self.driver.get(TEST_URL)
        header = HeaderPage(self.driver)
        self.login(self.driver)
        assert test_user.get('name').lower() in header.text_profile_user.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_checkout_page(self):
        """Test 2"""
        header = HeaderPage(self.driver)
        card = CardPage(self.driver)
        module = ModulePage(self.driver)
        checkout = CheckoutPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        assert header.text_digit_cart_header
        header.click_cart()
        module.click_module_button_order()
        self.wait_client_loader(self.driver)
        self.login_checkout(self.driver)
        assert test_user.get('name').lower() in header.text_profile_user.lower()
        assert test_user.get('name').lower() in checkout.text_checkout_user_name.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_multi(self):
        """Test 3"""
        self.driver.get(TEST_URL)
        header = HeaderPage(self.driver)
        self.login_multi(self.driver)
        assert test_user.get('multi_name').lower() in header.text_profile_user.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_checkout_page(self):
        """Test 4"""
        header = HeaderPage(self.driver)
        card = CardPage(self.driver)
        module = ModulePage(self.driver)
        checkout = CheckoutPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        assert header.text_digit_cart_header
        header.click_cart()
        module.click_module_button_order()
        self.wait_client_loader(self.driver)
        self.login_multi_checkout(self.driver)
        assert test_user.get('multi_name').lower() in header.text_profile_user.lower()
        assert test_user.get('multi_name').lower() in checkout.text_checkout_user_name.lower()
