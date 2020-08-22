
import os
from settings.browser_setting import Browser
x = os.environ
print('-----------------------------------------------------------------------')
print('environ----', x)
print('-----------------------------------------------------------------------')
br = Browser()
print(br.get_driver_path())
print('-----------------------------------------------------------------------')
