import os


def get_browser():
    return 'chrome'

driver_name = {'chrome': 'chromedriver.exe',
               'firefox': 'geckodriver.exe'
               }

drivers_dir = {'windows': os.path.abspath('../drivers/'),
               'linux': os.environ['HOME'] + '/virtualenv/python3.6.7/bin/'
               }

r = os.path.join(drivers_dir['linux'], driver_name[get_browser()][:-4])
print(r)
"""-A /home/travis/build/ulko81/project/report.html"""