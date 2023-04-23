import numpy as np
import interpolation
import values

print("Wybierz jedna z funkcji: ")
print("1. Liniowa:  y = 2x+2")
print("2. Wielomian:  y = -4x^3+2x^2-x+4")
print("3. Trygonometryczna:  y = -3*sin(2*x-1) ")
print("4. Złożenie:  y = cos(x) * x^3")
print("5. |x|")


user_input = int(input())
match user_input:
    case 1:
        type_of_func = 1
    case 2:
        type_of_func = 2
    case 3:
        type_of_func = 3
    case 4:
        type_of_func = 4
    case 5:
        type_of_func = 5

    case _:
        print("Wybierz spośród podanych opcji!")


print("\n Podaj: \n")
a = int(input("Lewy kraniec przedziału: "))
b = int(input("Prawy kraniec przedziału: "))
n = int(input("Liczbe węzłów: "))

# Zadane punkty interpolacji
x = interpolation.chebyshev_nodes(a, b, n)

y = values.one_value(type_of_func, x)

# Punkty do interpolacji
t = np.linspace(a, b, 200)

# Wartości funkcji interpolującej
p = np.zeros(len(t))
for i in range(len(t)):
    p[i] = interpolation.newton_interpolation(x, y, t[i])

# Wykres funkcji interpolującej i danych
import matplotlib.pyplot as plt


plt.plot(t, values.one_value(type_of_func, t), label='f(x)')
plt.plot(t, p, label='interpolacja')
plt.scatter(x, y,  color="red", marker="D", zorder=2)
plt.legend()
plt.show()
