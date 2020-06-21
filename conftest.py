from settings.browser_setting import Browser
import pytest
from  py._xmlgen import html


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


def pytest_html_report_title(report):
   report.title = "Report From "

def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Ticket'))

