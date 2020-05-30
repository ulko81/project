import os


def get_browser():
    return 'chrome'

driver_name = {'chrome': 'chromedriver.exe',
               'firefox': 'geckodriver.exe'
               }

drivers_dir = {'windows': os.path.abspath('../drivers/'),
               'linux': '/virtualenv/python3.6.7/bin/'
               }

r = os.path.join(os.environ['HOME'], driver_name[get_browser()][:-4])
print(r)
