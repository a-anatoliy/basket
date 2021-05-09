from decimal import Decimal

from basket_pricer.catalogue import CatalogueProvider
from basket_pricer.offer import OfferProvider
from basket_pricer.offers import EveryXIsFree, Percentage
from basket_pricer.pricer import BasketPricer

CATALOGUE = CatalogueProvider(
    {
        "MilkyWay": Decimal("0.99"),
        "Cookies": Decimal("2.34"),
        "Fish": Decimal("3.91"),
        "Bear (Small)": Decimal("2.00"),
        "Bear (Medium)": Decimal("3.50"),
        "Bear (Large)": Decimal("5.30"),
    }
)

OFFERS = OfferProvider(
    {
        "MilkyWay": [EveryXIsFree(2)],
        "Fish": [Percentage(Decimal("25"))],
        "Bear (Medium)": [Percentage(Decimal("25"))],
        "Bear (Medium)": [EveryXIsFree(2)],
        "Fish": [EveryXIsFree(2)],
    }
)

TEST = {
    "1" : {
        "basket" : {"MilkyWay": 4, "Cookies": 1}
    },
    "2" : {
        "basket" : {"MilkyWay": 2, "Cookies": 1, "Fish": 6}
    },
    "3" : {
        "basket" : {"MilkyWay": 9}
    },
    "4" : {
        "basket" : {"Bear (Medium)": 20}
    }
}

splitLine = '--------------------------------------'

def print_prices(prices):
    """
    Print results of calculations.
    """
    print("Result prices")
    print(f'Sub Total: {prices["sub_total"]}')
    print(f' Discount: {prices["discount"]}')
    print(f'    Total: {prices["total"]}')


if __name__ == "__main__":
    print (splitLine)
    for k,v in TEST.items():
        print("\tBASKET",k,"DEMO:")
        basket = v.get('basket')
        # print (basket)
        pricer = BasketPricer(CATALOGUE, OFFERS)
        print_prices(pricer.calculate_basket_prices(basket))
        print (splitLine)