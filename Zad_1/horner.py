def horner_scheme(wsp, st, x):
    wynik = wsp[0]

    for i in range(1, int(st) + 1):
        wynik = wynik * x + wsp[i]

    return wynik

#wsp od najwyższego do najniższego
# if __name__ == "__main__":
#     print(horner_scheme([1, 2, 3], 2, 5))
