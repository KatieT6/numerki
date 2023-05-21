from math import exp, pi
from Nested import Nested
from Polynomial import Polynomial
from math import exp, pi
from Trigonometric import Trigonometric
from Newton_Cotes import newton_cotes
from Gauss_Hermite import gauss_hermite_quadrature


poly1 = Polynomial([2, 2])  # 2x+2
poly2 = Polynomial([2, 1, -3])  # 4x^3+2x^2-x+4
trig1 = Trigonometric(3, 1, pi / 2)  # -3*sin(2*x-1)
trig2 = Trigonometric(2, 1, pi/2 - 1) #2*cos(x-1)

functions = (
    poly1,
    trig1,
    Nested([trig1, poly1]),
    lambda x: poly2(x) + trig2(x)
)

def weight(x): return exp(-x * x)

def _function():
    print("Wybierz jedna z funkcji: ")
    print("1. Liniowa:  y = 2x+2")
    print("2. Wielomian:  y = -4x^3+2x^2-x+4")
    print("3. Trygonometryczna:  y = -3*sin(2*x-1) ")
    print("4. Trygonometryczna:  y = 2*cos(x-1) ")

    a = int(input("===Wybor==="))

    if 5 > a > 0:
        return a - 1
    else:
        print("Zly wybor!")
        return _function()
def _nodes():
    nodes = int(input("Wprowadz liczbe wezlow (min 2, max 5): "))
    if 1 < nodes < 6:
        return nodes
    else:
        print("!!!Podano zla liczbe wezlow!!!")
    return _nodes()

if __name__ == '__main__':
    function = functions[_function()]
    eps = float(input("Podaj dokładnośc dla metody Newtona-Cortesa"))
    nodes = _nodes()

    result_n, intervals_n = newton_cotes(function, weight, eps)
    result_g = gauss_hermite_quadrature(nodes, function)

    print(
        f'Wynik dla metody Newtona-Cotesa: {result_n:.5f}; liczba przedzialow: {intervals_n}')
    print(f'Wynik dla metody Gaussa: {result_g:.5f}')
