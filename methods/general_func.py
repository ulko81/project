from helpers.dict_helper import *


def change_format_date_cart(date):
    if date.find('.') != -1:
        day = date[:date.find('.')]
        month = month_cart.get(date[3:5])
        time = date[10:].replace('\n', ' ')
        return '{} {}{}'.format(day, month, time)
    return date.replace('\n', ' ')


def change_format_price(price):
    if language_cur.get('ru') in price:
        count = price.find(language_cur.get('ru')) + 3
        price = price[:count]
        return price


def get_vendor_code(trademark, trademark_with_vendor_code):
    return trademark_with_vendor_code.replace(trademark, '').strip()
