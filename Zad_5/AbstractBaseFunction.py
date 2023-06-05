from abc import ABC, abstractmethod
from Exponentation import NumericType



class AbstractBaseFunction(ABC):
    @abstractmethod
    def __call__(self, argument: NumericType) -> NumericType:
        pass
