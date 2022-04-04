from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass

    def getCreatorCurrency(self) -> str:
        result = f'Getting the Creator currency - '