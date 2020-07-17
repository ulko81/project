import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as Chrome
from selenium.webdriver.firefox.options import Options as Firefox


class Browser:
    BROWSER_NAME = 'chrome'

    driver_name = {'chrome': 'chromedriver.exe',
                   'firefox': 'geckodriver.exe'
                  }

    drivers_dir = {'windows': os.path.abspath('../drivers/'),
                   'linux': '/virtualenv/python3.6.7/bin/'
                  }

    def get_driver_path(self):
        if os.name == 'posix':
            return os.path.join(os.environ['HOME'] + self.drivers_dir['linux'], self.driver_name[self.get_browser][:-4])
        else:
            return os.path.join(self.drivers_dir['windows'], self.driver_name[self.get_browser])

    def set_chrome(self, width=1920, height=1080, page_load_strategy='normal'):
        chrome_options = Chrome()
        capabilities = DesiredCapabilities.CHROME
        capabilities["pageLoadStrategy"] = page_load_strategy
        chrome_options.add_argument('--window-size={width_},{height_}'.format(width_=width, height_=height))
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities,
                                executable_path=self.get_driver_path())

    def set_firefox(self, width=1920, height=1080):
        firefox_options = Firefox()
        caps = DesiredCapabilities.FIREFOX
        firefox_options.add_argument('--window-size={width_},{height_}'.format(width_=width, height_=height))
        return webdriver.Firefox(firefox_options=firefox_options, desired_capabilities=caps,
                                 executable_path=self.get_driver_path())


    @property
    def get_browser(self):
        return os.environ.get('BROWSER') if os.environ.get('CI') else self.BROWSER_NAME

