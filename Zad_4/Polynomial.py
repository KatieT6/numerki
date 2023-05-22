from horner import horner_scheme
from typing import List

from AbstractBaseFunction import AbstractBaseFunction
from Exponentation import NumericType


class Polynomial(AbstractBaseFunction):
    def __init__(self, coefficients: List[NumericType]) -> None:
        super().__init__()
        self.coefficients = coefficients

    def __call__(self, argument: NumericType) -> NumericType:
        return horner_scheme(argument, self.coefficients)