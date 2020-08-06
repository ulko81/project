import os
from pages.header_page import HeaderPage
from pages.checkout_page import CheckoutPage
from pages.module_page import ModulePage


class AuthorizationMethod:

    @property
    def get_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import user_login
            return user_login

    @property
    def get_multi_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import multi_user_login
            return multi_user_login

    @property
    def get_password(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_PASS')
        else:
            from settings.user_setting import user_pass
            return user_pass

    def login(self, driver, login=None, password=None):
        if not login:
            login = self.get_username
            password = self.get_password
        header = HeaderPage(driver)
        module = ModulePage(driver)
        header.click_empty_profile()
        module.fill_module_phone_field(login)
        module.fill_module_pass_field(password)
        module.click_module_enter()

    def login_multi(self, driver, login=None, password=None):
        if not login:
            login = self.get_multi_username
            password = self.get_password
        header = HeaderPage(driver)
        module = ModulePage(driver)
        header.click_empty_profile()
        module.fill_module_phone_field(login)
        module.fill_module_pass_field(password)
        module.click_module_enter()
        button = header.get_first_multi_users()
        button.click()

    def login_checkout(self, driver, login=None, password=None):
        if not login:
            login = self.get_username
            password = self.get_password
        checkout = CheckoutPage(driver)
        checkout.fill_checkout_phone_field(login)
        checkout.fill_checkout_pass_field(password)
        checkout.click_checkout_enter()

    def login_multi_checkout(self, driver, login=None, password=None):
        if not login:
            login = self.get_multi_username
            password = self.get_password
        checkout = CheckoutPage(driver)
        checkout.fill_checkout_phone_field(login)
        checkout.fill_checkout_pass_field(password)
        checkout.click_checkout_enter()
        button = checkout.get_first_multi_users()
        button.click()
