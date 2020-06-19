import pytest
from pages.header import HeaderPage
from pages.checkout import CheckoutPage
from pages.card import CardPage
from settings.project_setting import TEST_URL, test_user, project_page
from methods.general_method import GeneralMethod


@pytest.mark.usefixtures('get_driver')
class TestAuthorization(GeneralMethod):

    @pytest.mark.auth
    def test_auth_simple(self):
        self.driver.get(TEST_URL)
        header_profile = HeaderPage(self.driver)
        self.login(self.driver)
        assert test_user.get('name').lower() in header_profile.text_profile_user.lower()

    @pytest.mark.auth
    def test_auth_checkout_page(self):
        header = HeaderPage(self.driver)
        card = CardPage(self.driver)
        checkout = CheckoutPage(self.driver)
        self.driver.get(TEST_URL + project_page.get('product_card'))
        card.click_button_buy()
        assert header.text_digit_cart_header
        header.click_cart_in_header()
        header.click_module_button_order()
        self.wait_client_loader(self.driver)
        self.login_checkout(self.driver)
        assert test_user.get('name').lower() in header.text_profile_user.lower()
        assert test_user.get('name').lower() in checkout.text_checkout_user_name.lower()