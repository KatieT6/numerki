# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
import horner
import bisection
import value_of_functions
import polynomial
import secant

#
print("1. Wielomianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")


def print_poly(coeff, stopien, a, b, xy_b, xy_s):
    # p = np.poly1d(coeff)
    # print(p)
    x = np.arange(a, b, 0.01)
    fx = value_of_functions.value_of_poly(coeff, x, stopien)

    plt.xlabel("oś X")
    plt.ylabel("oś Y")

    plt.xticks([i for i in range(int(a), int(b), 2)])
    plt.yticks([i for i in range(-10, 10, 2)])
    plt.grid()
    plt.xlim(a, b)
    plt.ylim(-10, 10)

    plt.plot(x, fx)
    if xy_b != 0 and xy_s != 0:
        plt.scatter([xy_b[0]], [xy_b[1]], color="red", marker="D", zorder=2)
        plt.scatter([xy_s[0]], [xy_s[1]], color="green", marker="D", zorder=3)

    plt.show()


def print_function(choice, a, b, xy_b, xy_s):
    x = np.arange(a, b, 0.01)
    fx = value_of_functions.values_of_func(choice, x)

    plt.xlabel("oś X")
    plt.ylabel("oś Y")

    plt.xticks([i for i in range(int(a), int(b), 2)])
    plt.yticks([i for i in range(-10, 10, 2)])

    plt.grid()
    plt.autoscale(enable=True)

    plt.plot(x, fx)
    if xy_b != 0 and xy_s != 0:
        plt.scatter([xy_b[0]], [xy_b[1]], color="red", marker="D", zorder=2)
        plt.scatter([xy_s[0]], [xy_s[1]], color="green", marker="D", zorder=3)

    plt.show()


def root_method(func_choice, a, b, coefficient, st):
    print(" a) spełnienie warunku nałożonego na dokładność \n b) osiągnięcie zadanej liczby iteracji")
    choose_method = input("Wybierz kryterium zatrzymania algorytmu:")

    match choose_method:
        case "a":
            epsilon = float(input("Podaj dokladnosc: \n"))
            # metoda bisekcji
            print("\nBisekcja: ")
            xy_b = bisection.bisect_method_accuracy(func_choice, epsilon, a, b, coefficient)
            print(xy_b)

            # metoda siecznych
            print("\nSiecznych: ")
            xy_s = secant.secant_method_accuracy(func_choice, a, b, epsilon, coefficient, st)
            print(xy_s)

            return xy_b, xy_s

        case "b":
            iterations = int(input("Podaj liczbe iteracji: \n"))
            # metoda bisekcji
            print("\nBisekcja: ")
            xy_b = bisection.bisect_method_iteration(func_choice, iterations, a, b, coefficient)
            print(xy_b)
            # metoda siecznych
            print("\nSiecznych: ")
            xy_s = secant.secant_method_iteration(func_choice, a, b, iterations, coefficient, st)
            print(xy_s)

            return xy_b, xy_s


def _range_(func_type, coeff, n):
    print("Okresl przedział [a, b]: ")
    x1 = float(input("Wprowadź początek przedziału, a: "))
    x2 = float(input("Wprowadź koniec przedziału, b: "))

    if func_type == 0:
        if horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) < 0:
            return x1, x2

        elif horner.horner_scheme(coeff, n, x1) * horner.horner_scheme(coeff, n, x2) > 0:
            return _range_(func_type, coeff, n)

    elif func_type != 0:
        if value_of_functions.one_value(func_type, x1) * value_of_functions.one_value(func_type, x2) < 0:
            return x1, x2

        elif value_of_functions.one_value(func_type, x1) * value_of_functions.one_value(func_type, x2) > 0:
            return _range_(func_type, coeff, n)


user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        coefficient, st = polynomial.polynomial_coefficients()
        print_poly(coefficient, st, -20, 20, 0, 0)
        x1, x2 = _range_(0, coefficient, st)
        xyb, xys = root_method(0, x1, x2, coefficient, st)
        print(f"Bisekcja: {xyb}\nSiecznych: {xys}")
        print_poly(coefficient, st, x1, x2, xyb, xys)

    case 2:
        print("Trygonometryczna")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = -3*sin(2*x-1) \n 2. y = cos(2*x-sin(-x))\n"))
        print_function(type_of_func, -20, 20, 0, 0)
        x1, x2 = _range_(type_of_func, 0, 0)
        xyb, xys = root_method(type_of_func, x1, x2, 0, 0)
        print_function(type_of_func, x1, x2, xyb, xys)

    case 3:
        print("Wykladnicza")
        type_of_func = int(input("Wybierz rodzaj: \n 3. y = 2^x-3 \n 4. y = 3^(2*x)-6\n"))
        print_function(type_of_func, -6, 1, 0, 0)
        x1, x2 = _range_(type_of_func, 0, 0)
        xyb, xys = root_method(type_of_func, x1, x2, 0, 0)
        print_function(type_of_func, x1, x2, xyb, xys)
    case _:
        print("Wybierz z pośród podanych opcji!")
