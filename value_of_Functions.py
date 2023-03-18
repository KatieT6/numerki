import horner
import numpy as np

functions = ["-3*sin(2*x-1)", "cos(2*x-sin(-x))", "5**x-3", "3**(2*x)-3"]


def value_of_poly(coeff, x, stopien):
    f = []
    for i in x:
        value = horner.horner_scheme(coeff, stopien, i)
        f.append(value)
    return f


# def one_value(choice, x):
#     if choice == 1:
#         return (-3) * np.sin(2 * x - 1)
#
#     if choice == 2:
#         return np.cos(2 * x - np.sin(-x))
#
#     if choice == 3:
#         return (5 ** x) - 3
#
#     if choice == 4:
#         return (3 ** (2 * x)) - 6

def one_value(choice, x):
    def f(x):
        f = eval(functions[choice - 1])
        return f

    return f(x)


# funkcja okreslajaca zboir wartosci dla danych x-ów
def values_of_func(choice, x):
    f = []
    for i in x:
        value = one_value(choice, i)
        f.append(value)
    return f
