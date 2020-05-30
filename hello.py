import os

driver_name = {'chrome': 'chromedriver.exe',
               'firefox': 'geckodriver.exe'
               }

drivers_dir = {'windows': os.path.abspath('../drivers/'),
               'linux': '/home/travis/virtualenv/python3.6.7/bin/'
               }

r = os.path.join(os.environ['HOME'], drivers_dir['linux'], driver_name['chrome'][:-4])
print(r)
