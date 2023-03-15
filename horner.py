def horner(wsp, st, x):
    wynik = wsp[0]

    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]

    return wynik


if __name__ == "__main__":
    print(horner([2, 2, 10, 5], 3, 5))
