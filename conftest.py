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

from datetime import datetime
import pytest

def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)



