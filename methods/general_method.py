import os
from pages.header import HeaderPage
from settings.user_setting import user_login, user_pass


class GeneralMethod:

    @property
    def get_username(self):
        if os.environ.get('CI'):
            return os.environ.get('USER_LOGIN')
        else:
            from settings.user_setting import user_login
            return user_login

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
        header.click_empty_profile()
        header.fill_module_phone_field(login)
        header.fill_module_pass_field(password)
        header.click_module_enter()






