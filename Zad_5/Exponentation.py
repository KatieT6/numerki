from typing import List

NumericType = int | float


def exponentation(base: NumericType, exponent: int) -> NumericType:
    if exponent == 0:
        return 1
    y = 1
    while exponent > 1:
        if exponent % 2:  # odd
            y = y * base
            base = base * base
            exponent = (exponent - 1) // 2
        else:  # even
            base = base * base
            exponent //= 2
    return base * y
