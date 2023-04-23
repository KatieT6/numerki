import numpy as np


def one_value(choice, x):
    if choice == 1:
        return 2*x+2

    if choice == 2:
        return -4 * x**3 + 2 * x**2 - x + 4

    if choice == 3:
        return -3 * np.sin(2*x-1)

    if choice == 4:
        return np.cos(x) * x**3

    if choice == 5:
        return np.abs(x)
    if choice == 6:
        return np.sin(x - 2) * x ** 2 - 3 * x

    # rint("1. Liniowa:  y = 2x+2")
    # print("2. Wielomian:  y = -4x^3+2x^2-x+4")
    # print("3. Trygonometryczna:  y = -3*sin(2*x-1) ")
    # print("4. Złożenie:  y = cos(x) * x^3")
    # print("|x|")