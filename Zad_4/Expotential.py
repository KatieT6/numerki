from AbstractBaseFunction import AbstractBaseFunction
from horner_exponentation import NumericType, quick_power


class Exponential(AbstractBaseFunction):
    '''
    Exponential function of the form f(x) = A ^ x
    '''

    def __init__(self, A) -> None:
        super().__init__()
        self.A = A

    def __call__(self, argument: NumericType) -> NumericType:
        if argument is int:
            return quick_power(self.A, argument)

        return self.A ** argument
