from math import exp, pi
from Modulus import Modulus
from Nested import Nested
from Polynomial import Polynomial
from Trigonometric import Trigonometric

ERROR_MSG = '\x1B[91mNiepoprawny wybor!\x1B[0m'


def weight(x): return exp(-x * x)


poly1 = Polynomial([1, 4])  # x + 4
trig1 = Trigonometric(1, 1, 0)  # 0.3 * cos(x)
poly2 = Polynomial([2, 1, -3])  # 2x^2 + x - 3
trig2 = Trigonometric(0.6, 0.2, 0.3)
mod = Modulus(1, 5, 8)  # 2 * | 5x + 8 |

functions = (
    poly1,
    trig1,
    Nested([trig1, poly1]),
    lambda x: poly2(x) + trig2(x),
    mod
)


def prompt_main():
    print("Podaj sposob aproksymacji: ")
    print("1. Wyznaczanie wielomianu aproksymacji podanego stopnia")
    print("2. Wyznaczenie wielomianu aproksymacji na podstawie oczekiwanego błedu")
    c = int(input("Wybor: "))

    function = functions[prompt_function()]
    left, right = prompt_range()

    if c == 2:
        error = prompt_error()
        nodes = prompt_nodes()
        return 2, function, left, right, error, nodes
    else:
        degree = prompt_degree()
        nodes = prompt_nodes()
        return 1, function, left, right, degree, nodes


def prompt_function():
    print("dostepne funkcje: ")
    print("1. f(x) = x+4")
    print("2. f(x) = 0.3 * cos(x)")
    print("3. f(x) = 3 * (0.3cos(x))^3 + 2 * (0.3cos(x))^2 + 0.3cos(x) + 4")
    print("4. f(x) = 2x^2 + x - 3 + 0.6 * sin(0.2 * x + 0.3)")
    print("5. f(x) = 1 * | 5x + 8 |")
    ch = input("Wybor: ")
    print("================")

    if ch in "12345":
        return int(ch) - 1
    else:
        print(ERROR_MSG)
        return prompt_function()


def prompt_range():
    left = float(input("Podaj lewy przedzial aproksymacji: "))
    right = float(input("Podaj prawy przedzial aproksymacji: "))
    return left, right


def prompt_error():
    error = float(input("Podaj oczekiwany blad aproksymacji: "))
    return error


def prompt_degree():
    degree = int(input("Podaj stopień wielomianu aproksymującego: "))
    return degree


def prompt_nodes():
    nodes = int(input("Wprowadz liczbe wezlow (2 - 5): "))
    print("================")
    if 1 < nodes < 6:
        return nodes

    print(ERROR_MSG)
    return prompt_nodes()
