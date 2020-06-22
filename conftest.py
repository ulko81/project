from datetime import datetime
from settings.browser_setting import Browser
import pytest


browser = {
    'chrome': Browser().set_chrome,
    'firefox': Browser().set_firefox
}


@pytest.fixture()
def get_driver(request):
    driver = browser[Browser().get_browser]()
    request.cls.driver = driver

    def close_driver():
        driver.quit()
    request.addfinalizer(close_driver)


def pytest_html_report_title(report):
   report.title = "Report From {}".format(datetime.today().strftime('%d-%m-%Y'))


