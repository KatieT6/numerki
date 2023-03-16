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
        a.append(int(input("Podaj współczynnik a" + str(i) + ": ")))
        print("to jest a dla x" + str(i) + ": " + str(a))
    return a, stopien


def value_of_poly(coeff, x, stopien):
    f = []
    for i in x:
        value = horner.horner_scheme(coeff, stopien, i)
        f.append(value)
    return f


def print_poly(coeff, stopien):
    # p = np.poly1d(coeff)
    # print(p)
    x = np.arange(-20, 20, 0.01)
    fx = value_of_poly(coeff, x, stopien)

    plt.xlabel("oś X")
    plt.ylabel("oś Y")

    plt.xticks([i for i in range(-20, 20, 5)])
    plt.yticks([i for i in range(-20, 20, 5)])
    plt.grid()
    plt.xlim(-20, 20)
    plt.ylim(-10, 20)
    plt.plot(x, fx)
    plt.show()


def value_of_func(choice, x):
    f = []
    # 1. y = -3*sin(2*x-1)
    if choice == 1:
        for i in x:
            value = (-3) * np.sin(2 * i - 1)
            f.append(value)
        return f

    # 2. y = cos(2*x-sin(-x))
    elif choice == 2:
        for i in x:
            value = np.cos(2 * i - np.sin(-i))
            f.append(value)
        return f

    # 3. y = 5^x-3
    elif choice == 3:
        for i in x:
            value = (5**i)-3
            f.append(value)
        return f

    # 4. y = 3^(2*x)-6
    elif choice == 4:
        for i in x:
            value = (3**(2*i))-6
            f.append(value)
        return f


def print_function(choice):
    x = np.arange(-20, 20, 0.01)
    fx = value_of_func(choice, x)

    plt.xlabel("oś X")
    plt.ylabel("oś Y")

    # plt.xticks([i for i in range(-20, 20, 5)])
    # plt.yticks([i for i in range(-20, 20, 5)])

    plt.xticks()

    plt.grid()

    plt.autoscale(enable=True)

    # plt.xlim(-20, 20)
    # plt.ylim(-10, 20)
    plt.plot(x, fx)

    plt.show()


user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        coefficient, st = polynomial_coefficients()
        print_poly(coefficient, st)
        x1, x2 = rage()
        # bisekcja.bisect_method_accuracy()

    case 2:
        print("Trygonometryczna")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = -3*sin(2*x-1) \n 2. y = cos(2*x-sin(-x))"))
        print_function(type_of_func)
        #x1, x2 = rage()

    case 3:
        print("Wykladnicza")
        type_of_func = int(input("Wybierz rodzaj: \n 3. y = 5^x-3 \n 4. y = 3^(2*x)-3"))
        print_function(type_of_func)
        #x1, x2 = rage()
    case _:
        print("Dokonaj wyboru")