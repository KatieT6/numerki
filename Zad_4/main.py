from math import exp, pi


print("Wybierz jedna z funkcji: ")
print("1. Liniowa:  y = 2x+2")
print("2. Wielomian:  y = -4x^3+2x^2-x+4")
print("3. Trygonometryczna:  y = -3*sin(2*x-1) ")
print("4. Trygonometryczna:  y = 2*cos(x-1) ")


a = int(input("===Wybor==="))

eps = int(input("Podaj dokładnośc dla metody Newtona-Cortesa"))
