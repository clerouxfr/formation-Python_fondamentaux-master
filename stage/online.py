
"""
PRICE_FR = "Prix : {:10} {:.2}"
PRICE_US = "Price : {:10} {:.2}"
CURRENCY_EU = "Euros"
CURRENCY_US = "Dollars"
"""

PRICE_FR = "Prix : {} {:.2}"
PRICE_US = "Price : {1} {0:.2}"
CURRENCY_EU = "Euros"
CURRENCY_US = "Dollars"


def display_price(template, price, currency):
    print(template.format(price, currency))


display_price(PRICE_FR, 42, CURRENCY_EU)

display_price(PRICE_US, 56.344, CURRENCY_US)