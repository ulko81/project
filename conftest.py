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
    driver.get(Browser().default_url)
    def close_driver():
        driver.close()
    request.addfinalizer(close_driver)


