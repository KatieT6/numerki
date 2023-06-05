from math import isclose
from typing import Tuple

from AbstractBaseFunction import AbstractBaseFunction


def simpson(
        left: float,
        right: float,
        function: AbstractBaseFunction,
        weight) -> float:

    h = 0.5 * (right - left)
    mid = 0.5 * (left + right)

    val = (h / 3) * (weight(left) * function(left)
                     + 4 * weight(mid) * function(mid)
                     + weight(right) * function(right))

    return val


def complex_simpson(
        left: float,
        right: float,
        function: AbstractBaseFunction,
        weight,
        epsilon,
        doubleNumberOfIntervals=True) -> Tuple[float, int]:

    prev = simpson(left, right, function, weight)
    n = 2

    accuracyConditionMet = False

    while not(accuracyConditionMet):
        newValue = 0
        t = (right - left) / n
        for i in range(n):
            newValue += simpson(left + i * t,
                                left + t * (i + 1),
                                function,
                                weight)

        if isclose(newValue, prev, abs_tol=epsilon):
            accuracyConditionMet = True
        else:
            if doubleNumberOfIntervals:
                n = n * 2
            else:
                n = n + 1

        prev = newValue

    return prev, n


def newton_cotes(
        function: AbstractBaseFunction,
        weight,
        epsilon: float) -> float:

    a = 1
    n1 = n2 = 0

    # result for interval [0, inf)
    result1, n1 = complex_simpson(0, a, function, weight, epsilon)
    delta = 0.5

    limitFound = False

    while not limitFound:
        t, tn = complex_simpson(a, a + delta, function, weight, epsilon)
        n1 = max(tn, n1)
        result1 += t
        if abs(t) <= epsilon:
            limitFound = True
        else:
            a = a + delta

    # result for interval (-inf, 0]
    a = 1
    result2, n2 = complex_simpson(-a, 0, function, weight, epsilon)
    limitFound = False

    while not limitFound:
        t, tn = complex_simpson(-(a + delta), -a, function, weight, epsilon)
        n2 = max(tn, n2)
        result2 += t
        if abs(t) <= epsilon:
            limitFound = True
        else:
            a = a + delta

    return result1 + result2, max(n1, n2)
