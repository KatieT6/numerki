from math import sin

from AbstractBaseFunction import AbstractBaseFunction
from Exponentation import NumericType

class Trigonometric(AbstractBaseFunction):
    """
    Trigonometric function of the form f(x) = A * sin(B * x + C)
    """

    def __init__(self, A: NumericType, B: NumericType, C: NumericType):
        super().__init__()
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, argument: NumericType) -> NumericType:
        return self.A * sin(self.B * argument + self.C)