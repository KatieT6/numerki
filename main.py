# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import horner
import bisection

#
print("1. Wielomianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")





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


# funkcja do obliczania wartości wybranej funkcji dla danego x
def one_value(choice, x):
    if choice == 1:
        return (-3) * np.sin(2 * x - 1)

    if choice == 2:
        return np.cos(2 * x - np.sin(-x))

    if choice == 3:
        return (5 ** x) - 3

    if choice == 4:
        return (3 ** (2 * x)) - 6


# funkcja okreslajaca zbir wartosci dla danych x-ów
def value_of_func(choice, x):
    f = []
    for i in x:
        value = one_value(choice, i)
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


def zero_point_method():
    print(" a) spełnienie warunku nałożonego na dokładność \n b) osiągnięcie zadanej liczby iteracji")
    choose_method = int(input("Wybierz wybiera kryterium zatrzymania algorytmu:"))
    match choose_method:
        case "a":
            epsilon = float(input("Podaj dokladnosc:"))
            # metoda bisekcji
            #bisection.bisect_method_accuracy()
            # metoda siecznych
        case "b":
            iterations = int(input("Podaj liczbe iteracji:"))
            # metoda bisekcji

            # metoda siecznych


def rage(func_type, coeff, n):
    print("Okresl przedział: ")
    x1 = float(input("Wprowadź początek przedziału: "))
    x2 = float(input("Wprowadź koniec przedziału: "))

    if func_type == 0:
        if horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) < 0:
            return x1, x2

        elif horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) > 0:
            return rage(func_type, coeff, n)

    elif func_type != 0:
        if one_value(func_type, x1) * one_value(func_type, x2) < 0:
            return x1, x2

        elif one_value(func_type, x1) * one_value(func_type, x2) > 0:
            return rage(func_type, coeff, n)


user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        coefficient, st = polynomial_coefficients()
        print_poly(coefficient, st)
        x1, x2 = rage(0, coefficient, st)
        zero_point_method()

    case 2:
        print("Trygonometryczna")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = -3*sin(2*x-1) \n 2. y = cos(2*x-sin(-x))"))
        print_function(type_of_func)
        x1, x2 = rage(type_of_func, 0, 0)

    case 3:
        print("Wykladnicza")
        type_of_func = int(input("Wybierz rodzaj: \n 3. y = 5^x-3 \n 4. y = 3^(2*x)-3"))
        print_function(type_of_func)
        x1, x2 = rage(type_of_func, 0, 0)
    case _:
        print("Wybierz z pośród podanych opcji!")
