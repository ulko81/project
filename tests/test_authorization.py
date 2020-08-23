import pytest
from pages.header_page import HeaderPage
from pages.checkout_page import CheckoutPage
from pages.card_page import CardPage
from pages.module_page import ModulePage
from settings.project_setting import TEST_URL, test_user
from settings.project_page import project_page
from methods.authorization_method import AuthorizationMethod


@pytest.mark.usefixtures('get_driver')
class TestAuthorization(AuthorizationMethod):

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_simple(self):
        self.driver.get(TEST_URL)
        header_profile = HeaderPage(self.driver)
        self.login(self.driver)
        assert test_user.get('name').lower() in header_profile.text_profile_user.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_checkout_page(self):
        header = HeaderPage(self.driver)
        card = CardPage(self.driver)
        module_cart = ModulePage(self.driver)
        checkout = CheckoutPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        assert header.text_digit_cart_header
        header.click_cart()
        module_cart.click_module_button_order()
        self.wait_client_loader(self.driver)
        self.login_checkout(self.driver)
        assert test_user.get('name').lower() in header.text_profile_user.lower()
        assert test_user.get('name').lower() in checkout.text_checkout_user_name.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_multi(self):
        self.driver.get(TEST_URL)
        header_profile = HeaderPage(self.driver)
        self.login_multi(self.driver)
        assert test_user.get('multi_name').lower() in header_profile.text_profile_user.lower()

    @pytest.mark.smoke
    @pytest.mark.auth
    def test_auth_checkout_page(self):
        header = HeaderPage(self.driver)
        card = CardPage(self.driver)
        module_cart = ModulePage(self.driver)
        checkout = CheckoutPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card_with_offers'))
        card.click_button_buy()
        assert header.text_digit_cart_header
        header.click_cart()
        module_cart.click_module_button_order()
        self.wait_client_loader(self.driver)
        self.login_multi_checkout(self.driver)
        assert test_user.get('multi_name').lower() in header.text_profile_user.lower()
        assert test_user.get('multi_name').lower() in checkout.text_checkout_user_name.lower()
