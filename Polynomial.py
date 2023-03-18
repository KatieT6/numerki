import numpy as np
def polynomial_coefficients():
    stopien = int(input("Wprowadz stopien wielomianu: "))
    a = []
    for i in reversed(range(0, stopien + 1)):
        a.append(int(input("Podaj współczynnik a" + str(i) + ": ")))
        print("to jest a dla x" + str(i) + ": " + str(a))
    return a, stopien

def polynomial_to_string(coeff, stopien):
    p1 = np.polynomial.Polynomial(coeff)
    # for i in range(len(coeff)):
    #     print(coeff[i])
    print(p1)
