from settings.browser_setting import Browser
import pytest
import time
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

@pytest.fixture()
def delay():
    time.sleep(10)

import pytest
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra



