# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import horner
import bisection
import value_of_Functions
import Polynomial
import Secant

#
print("1. Wielomianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")


def print_poly(coeff, stopien):
    # p = np.poly1d(coeff)
    # print(p)
    x = np.arange(-20, 20, 0.01)
    fx = value_of_Functions.value_of_poly(coeff, x, stopien)

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



def print_function(choice):
    x = np.arange(-20, 20, 0.01)
    fx = value_of_Functions.values_of_func(choice, x)

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


def zero_point_method(func_choice, a, b):
    print(" a) spełnienie warunku nałożonego na dokładność \n b) osiągnięcie zadanej liczby iteracji")
    choose_method = int(input("Wybierz wybiera kryterium zatrzymania algorytmu:"))
    match choose_method:
        case "a":
            epsilon = float(input("Podaj dokladnosc:"))
            # metoda bisekcji
            print("Bisekcja: ")
            print(bisection.bisect_method_accuracy(func_choice, epsilon, a, b, coefficient))

            # metoda siecznych
            print("\nSiecznych: ")
            print(Secant.secant_method_accuracy(func_choice, a, b, epsilon, coefficient, st))


        case "b":
            iterations = int(input("Podaj liczbe iteracji:"))
            # metoda bisekcji
            print("Bisekcja: ")
            print(bisection.bisect_method_iteration(func_choice, iterations, a, b, coefficient))

            # metoda siecznych
            print("\nSiecznych: ")
            print(Secant.secant_method_iteration(func_choice, a, b, iterations, coefficient, st))


def _range_(func_type, coeff, n):
    print("Okresl przedział: ")
    x1 = float(input("Wprowadź początek przedziału: "))
    x2 = float(input("Wprowadź koniec przedziału: "))

    if func_type == 0:
        if horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) < 0:
            return x1, x2

        elif horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) > 0:
            return _range_(func_type, coeff, n)

    elif func_type != 0:
        if value_of_Functions.one_value(func_type, x1) * value_of_Functions.one_value(func_type, x2) < 0:
            return x1, x2

        elif value_of_Functions.one_value(func_type, x1) * value_of_Functions.one_value(func_type, x2) > 0:
            return _range_(func_type, coeff, n)


user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        coefficient, st = Polynomial.polynomial_coefficients()
        Polynomial.polynomial_to_string(coefficient, st)
        print_poly(coefficient, st)
        x1, x2 = _range_(0, coefficient, st)
        zero_point_method(0, x1, x2)

    case 2:
        print("Trygonometryczna")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = -3*sin(2*x-1) \n 2. y = cos(2*x-sin(-x))"))
        print_function(type_of_func)
        x1, x2 = _range_(type_of_func, 0, 0)

    case 3:
        print("Wykladnicza")
        type_of_func = int(input("Wybierz rodzaj: \n 3. y = 5^x-3 \n 4. y = 3^(2*x)-3"))
        print_function(type_of_func)
        x1, x2 = _range_(type_of_func, 0, 0)
    case _:
        print("Wybierz z pośród podanych opcji!")
