import numpy as np


def chebyshev_nodes(a, b, n):
    """
    Funkcja zwraca węzły Czebyszewa w przedziale [a, b]
    o liczbie węzłów n.
    """
    x = np.zeros(n)
    for i in range(n):
        x[i] = (a + b) / 2 + (b - a) / 2 * np.cos((2 * i + 1) * np.pi / (2 * n))
    return x


def divided_differences(x, y):
    """
    Funkcja zwraca ilorazy różnicowe dla węzłów x i wartości
    funkcji y.
    """
    n = len(x)
    f = np.zeros([n, n])
    for i in range(n):
        f[i, 0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i + 1, j - 1] - f[i, j - 1]) / (x[i + j] - x[i])
    return f[0]


def newton_interpolation(x, y, t):
    """
    Funkcja zwraca wartość funkcji interpolującej dla punktu t,
    wyznaczonej metodą interpolacji Newtona na węzłach Czebyszewa
    dla węzłów x i wartości funkcji y.
    """
    n = len(x)
    c = divided_differences(x, y)
    p = c[n - 1]
    for i in range(n - 2, -1, -1):
        p = c[i] + (t - x[i]) * p
    return p