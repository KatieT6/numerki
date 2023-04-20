def horner_scheme(wsp, st, x):
    wynik = wsp[0]

    for i in range(1, int(st) + 1):
        wynik = wynik * x + wsp[i]

    return wynik
