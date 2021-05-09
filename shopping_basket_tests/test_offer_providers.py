from decimal import Decimal

from basket_pricer.offer import OfferProvider
from basket_pricer.offers import Percentage


def test_offer_provider_get_offers_for_sku():
    provider = OfferProvider({"PAN": [Percentage(Decimal("10"))]})
    assert provider.get_offers("PAN") == [Percentage(Decimal("10"))]


def test_offer_provider_get_offers_for_sku_with_multiple_offers():
    provider = OfferProvider(
        {
            "PAN": [
                Percentage(Decimal("10")),
                Percentage(Decimal("5")),
            ]
        }
    )
    assert provider.get_offers("PAN") == [
        Percentage(Decimal("10")),
        Percentage(Decimal("5")),
    ]


def test_offer_provider_returns_empty_list_when_no_offers():
    provider = OfferProvider({"PAN": []})
    assert provider.get_offers("PAN") == []


def test_offer_provider_returns_empty_list_when_no_sku_if_products():
    provider = OfferProvider({})
    assert provider.get_offers("PAN") == []