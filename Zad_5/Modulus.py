from AbstractBaseFunction import AbstractBaseFunction
from utils import NumericType
from math import fabs


class Modulus(AbstractBaseFunction):
    """
    Modulus function of the form f(x) = A * |B * x + C|
    """

    def __init__(self, A: NumericType, B: NumericType, C: NumericType) -> None:
        super().__init__()
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, argument: NumericType) -> NumericType:
        return self.A * fabs(self.B * argument + self.C)
