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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        extra.append(pytest_html.extras.html('<p>some html</p>'))
        report.extra = extra


