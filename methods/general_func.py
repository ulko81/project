from helpers.month_cart_helper import month_cart


def change_format_date_cart(date):
    if date.find('.') != -1:
        day = date[:date.find('.')]
        month = month_cart.get(date[3:5])
        time = date[10:]
        return "{} {} {}".format(day, month, time)
    return date
