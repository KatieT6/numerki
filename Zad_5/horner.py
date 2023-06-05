NumericType = int | float
from typing import List

def horner_scheme(x: float, coefficients: List[NumericType]) -> NumericType:
    value = coefficients[0]

    for coef in coefficients[1:]:
        value = value * x + coef

    return value