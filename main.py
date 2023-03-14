# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt

print("1. Wielomianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")


def przedzial_poszukiwania():
    print("Okresl przedział: ")
    x1 = float(input("Wprowadź początek przedziału: "))
    x2 = float(input("Wprowadź koniec przedziału: "))
    return x1, x2


def wielomian_wspolczynniki():
    stopien = int(input("Wprowadz stopien wielomianu"))
    n = []
    for i in range(0, stopien + 1):
        n.append(input("Podaj współczynnik a" + str(i) + ": "))
        print("to jest a dla x" + str(i) + ": " + str(n))
    return n, stopien


def rysuj_wielomian(x1, x2, n, stopien):
    x = np.linspace(x1, x2)
    fx = []
    for i in range(len(x)):
        fx.append(n[stopien]*x[i]**stopien)


# def horner():


user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Wielomianowa")
        x1, x2 = przedzial_poszukiwania()
        wspolczynniki = wielomian_wspolczynniki()

    case 2:
        print("Trygonometryczna")
        x1, x2 = przedzial_poszukiwania()

    case 3:
        print("Wykladnicza")
        x1, x2 = przedzial_poszukiwania()
