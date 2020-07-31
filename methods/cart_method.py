from helpers.dict_helper import *


class CartMethod:

    @staticmethod
    def change_format_date_cart(date):
        if date.find('.') != -1:
            day = int(date[:date.find('.')])
            month = month_cart.get(date[3:5])
            time = date[10:].replace('\n', ' ')
            return '{} {}{}'.format(day, month, time)
        return date.replace('\n', ' ')
