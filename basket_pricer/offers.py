from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal

from basket_pricer.exceptions import OfferConfigurationException


class BaseOffer(ABC):
    @abstractmethod
    def calculate_discount(self, price: Decimal, quantity: int) -> Decimal:
        ...


@dataclass
class Percentage(BaseOffer):
    # Offer calculates percentage discount
    NotNegative = 'Could not be negative!'
    discount_percent: Decimal

    def calculate_discount(self, price: Decimal, quantity: int) -> Decimal:
        if self.discount_percent < Decimal("0"):
            raise OfferConfigurationException(NotNegative)
        if self.discount_percent > Decimal("100"):
            raise OfferConfigurationException('No more than 100%')

        return (price * quantity * self.discount_percent) / 100


@dataclass
class EveryXIsFree(BaseOffer):
    # Offer where after buying X product items next is free

    one_free_after: int

    def calculate_discount(self, price: Decimal, quantity: int) -> Decimal:
        if self.one_free_after < 0:
            raise OfferConfigurationException(NotNegative)
        number_of_free_products = quantity // (self.one_free_after + 1)
        return number_of_free_products * price