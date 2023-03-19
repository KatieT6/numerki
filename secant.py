import horner
import value_of_functions
import numpy as np


def secant_method_iteration(choice, x0, x1, iteration, coeff, stopien):
    # def f(x):
    #     f = eval(func)
    #     return f

    for i in range(1, iteration):

        if 4 >= choice >= 1:
            fx0 = value_of_functions.one_value(choice, x0)
            fx1 = value_of_functions.one_value(choice, x1)
        elif choice == 0:
            fx0 = horner.horner_scheme(coeff, stopien, x0)
            fx1 = horner.horner_scheme(coeff, stopien, x1)

        divider = x0 - x1
        if divider != 0:

            xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))

            x0 = x1
            x1 = xi
            print(f"{i}. The root was found to be at {xi}")

        elif divider == 0:
            print(f"It seems that the divider equals zero :(")

    fxi = 0
    if 4 >= choice >= 1:
        fxi = value_of_functions.one_value(choice, xi)
    elif choice == 0:
        fxi = horner.horner_scheme(coeff, stopien, xi)

    return xi, fxi


def secant_method_accuracy(choice, x0, x1, acc, coeff, stopien):
    # def f(x):
    #     f = eval(func)
    #     return f

    xi = 0

    if 4 >= choice >= 1:

        while np.abs(value_of_functions.one_value(choice, xi)) > acc:
            fx0 = value_of_functions.one_value(choice, x0)
            fx1 = value_of_functions.one_value(choice, x1)

            divider = x0 - x1

            if divider != 0:

                xi = x0 - (fx0 / ((fx0 - fx1) / divider))

                x0 = x1
                x1 = xi

                print(f"The root was found to be at {xi}")

            elif divider == 0:
                print(f"It seems that the divider equals zero :(")

        fxi = value_of_functions.one_value(choice, xi)
        return [xi, fxi]

    elif choice == 0:

        while np.abs(horner.horner_scheme(coeff, choice, xi)) > acc:
            fx0 = horner.horner_scheme(coeff, stopien, x0)
            fx1 = horner.horner_scheme(coeff, stopien, x1)

            divider = x0 - x1

            if divider != 0:

                xi = x0 - (fx0 / ((fx0 - fx1) / divider))

                x0 = x1
                x1 = xi

                print(f"The root was found to be at {xi}")

            elif divider == 0:
                print(f"It seems that the divider equals zero :(")
                fxi = horner.horner_scheme(coeff, choice, xi)
                return [xi, fxi]

