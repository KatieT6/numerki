import numpy as np
import horner

def one_value(choice, x):
    if choice == 1:
        return 2*x+2

    if choice == 2:
        return value_of_poly([-4,2,-1,4],x,3)

    if choice == 3:
        return -3 * np.sin(2*x-1)

    if choice == 4:
        return np.cos(x) * x**3

    if choice == 5:
        return np.abs(x)


def value_of_poly(coeff, x, stopien):
    f = []
    for i in x:
        value = horner.horner_scheme(coeff, stopien, i)
        f.append(value)
    return f