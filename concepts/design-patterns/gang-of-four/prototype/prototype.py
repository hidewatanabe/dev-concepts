

from abc import ABC
from math import prod


class Prototype(ABC):
    def clone(self) -> None:
        pass

class Message(Prototype):
    def __init__(self, action: str, product: str, price: float) -> None:
        self._action = action
        self._product = product
        self._price = price

    @property
    def action(self) -> str:
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        self._action = action

    @property
    def product(self) -> str:
        return self._product

    @product.setter
    def product(self, product: str) -> None:
        self._product = product

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price

    def clone(self) -> None:
        new = self.__class__(self.action, self.product, self.price)
        return new


if __name__ == '__main__':
    message = Message('create', 'instance', 10.)
    message_cloned = message.clone()

    message.action = 'update'

    message_cloned.price = 11.

    print(f'First message: {vars(message)}')
    print(f'Second message: {vars(message_cloned)}')

