from typing import List

from AbstractBaseFunction import AbstractBaseFunction
from horner_exponentation import *


class Polynomial(AbstractBaseFunction):
    def __init__(self, coefficients: List[NumericType]) -> None:
        super().__init__()
        self.coefficients = coefficients

    def __call__(self, argument: NumericType) -> NumericType:
        return horner_scheme(argument, self.coefficients)