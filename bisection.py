import numpy as np

import horner
import value_of_functions


def change_value_type_based(func, a, b, coeff, x0):
    if 1 <= func <= 4:
        funcx0 = value_of_Functions.one_value(func, x0)
        funcA = value_of_Functions.one_value(func, a)
        funcB = value_of_Functions.one_value(func, b)

    elif func <= 0:
        funcx0 = horner.horner_scheme(coeff, len(coeff) - 1, x0)
        funcA = horner.horner_scheme(coeff, len(coeff) - 1, a)
        funcB = horner.horner_scheme(coeff, len(coeff) - 1, b)

    return funcx0, funcA, funcB


def bisect_method_iteration(func, iteration, a, b, coeff):
    x0 = 0
    for i in range(iteration):
        x0 = (a + b) / 2
        funcx0, funcA, funcB = change_value_type_based(func, a, b, coeff, x0)

        if funcx0 * funcB < 0:
            a = x0
        elif funcx0 * funcA < 0:
            b = x0

    return [x0, funcx0]


# def bisect_method_accuracy(func, acc, a, b, coeff):
#     x0 = (a + b) / 2
#     funcx0, funcA, funcB = change_value_type_based(func, a, b, coeff, x0)
#     print(f"Bisekcja x0 {x0} fx: {funcx0}")
#     if np.abs(funcx0) <= acc:
#         return [x0, funcx0]
#     elif funcx0 * funcB < 0:
#         a = x0
#         bisect_method_accuracy(func, acc, a, b, coeff)
#     elif funcx0 * funcA < 0:
#         b = x0
#         bisect_method_accuracy(func, acc, a, b, coeff)

def bisect_method_accuracy(func, acc, a, b, coeff):
    x0 = (a + b) / 2
    funcx0, funcA, funcB = change_value_type_based(func, a, b, coeff, x0)
    while np.abs(funcx0) > acc:
        x0 = (a + b) / 2
        funcx0, funcA, funcB = change_value_type_based(func, a, b, coeff, x0)
        print(f"Bisekcja x0 {x0} fx: {funcx0}")
        if funcx0 * funcB < 0:
            a = x0

        elif funcx0 * funcA < 0:
            b = x0

    return [x0, funcx0]
