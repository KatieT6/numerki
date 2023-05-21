from typing import List

from AbstractBaseFunction import AbstractBaseFunction
from utils import NumericType


class Nested(AbstractBaseFunction):
    def __init__(self, functions: List[AbstractBaseFunction]) -> None:
        super().__init__()
        self.functions = functions

    def __call__(self, argument: NumericType) -> NumericType:
        for function in self.functions:
            argument = function(argument)

        return argument
