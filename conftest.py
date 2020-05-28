from settings.browser_settings import Browser
import pytest
browser = {
    'chrome':Browser().set_chrome,
    'firefox':Browser().set_firefox
}

@pytest.fixture()
def get_driver(request):
    driver = browser[Browser().get_browser]()
    request.cls.driver = driver
    def close_driver():
        driver.quit()
    request.addfinalizer(close_driver)


