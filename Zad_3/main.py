print("1. Liniowa")
print("2. Wielomian")
print("3. Trygonometryczna")
print("4. Złożenie")
print("5. |x|")

user_input = int(input("Wybierz jedna z funkcji: "))

match user_input:
    case 1:
        print("Liniowa")


    case 2:
        print("Wielomian")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = - interpolacyjny    \n 2. y = - interpolowany\n"))

    case 3:
        print("Trygonometryczna")
        type_of_func = int(input("Wybierz rodzaj: \n 1. y = -3*sin(2*x-1)    \n 2. y = cos(2*x-sin(-x))\n"))

    case 4:
        print("Złożenie")
        type_of_func = int(input("Wybierz rodzaj: \n 5. y = cos(x) * x^3  \n 6. y = sin(x-2)*x^2-3x\n"))

    case 5:
        print("|x|")

    case _:
        print("Wybierz z pośród podanych opcji!")