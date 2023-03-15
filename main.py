# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import horner
import bisekcja
#
print("1. Wielomianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")


def rage():
    print("Okresl przedział: ")
    x1 = float(input("Wprowadź początek przedziału: "))
    x2 = float(input("Wprowadź koniec przedziału: "))
    return x1, x2


def polynomial_coefficients():
    stopien = int(input("Wprowadz stopien wielomianu: "))
    a = []
    for i in reversed(range(0, stopien + 1)):
        a.append(input("Podaj współczynnik a" + str(i) + ": "))
        print("to jest a dla x" + str(i) + ": " + str(a))
    return a, stopien

def wartosc_func(coeff, x):
    f = []
    for i in x:
        value = horner.horner_scheme([1, 2, 3], 2, x)
        f.append(value)

    return f


def print_poly(coeff):
    p = np.poly1d([1, 2, 3])
    print(p)
    x = np.arange(-5, 5, 0.01)
    fx = wartosc_func([1, 2, 3], x)

    plt.xlabel("os X")
    plt.ylabel("os Y")

     plt.plot(x, [fx[i] for i in x])

    plt.xticks([i for i in range(-20, 20, 5)])
    plt.yticks([i for i in range(-20, 20, 5)])
    plt.grid()
    plt.xlim(-10, 10)
    plt.ylim(-5, 20)
    plt.plot(x, fx)
    plt.show()



user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        #x1, x2 = rage()
        #coefficient = polynomial_coefficients()[0]
        print_poly([1, 2, 3])
        #bisekcja.bisect_method_accuracy()

    case 2:
        print("Trygonometryczna")
        x1, x2 = rage()

    case 3:
        print("Wykladnicza")
        x1, x2 = rage()
