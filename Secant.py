import horner
import value_of_Functions

def secant_method_iteration(choice, x0, x1, iteration, coeff, stopien ):

             # def f(x):
             #     f = eval(func)
             #     return f

             for i in range(1, iteration):

                 if 4 >= choice >= 1:
                    fx0 = value_of_Functions.one_value(choice, x0)
                    fx1 = value_of_Functions.one_value(choice, x1)
                 elif choice == 0:
                     fx0 = horner.horner_scheme(coeff, stopien, x0)
                     fx1 = horner.horner_scheme(coeff, stopien, x1)

                 xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))

                 x0 = x1
                 x1 = xi
                 print(f"{i}. The root was found to be at {xi}")



def secant_method_accuracy(choice, x0, x1, acc, coeff, stopien ):
            # def f(x):
            #     f = eval(func)
            #     return f
            xi = 0

            while xi < acc:

                 if 4 >= choice >= 1:
                     fx0 = value_of_Functions.one_value(choice, x0)
                     fx1 = value_of_Functions.one_value(choice, x1)
                 elif choice == 0:
                     fx0 = horner.horner_scheme(coeff, stopien, x0)
                     fx1 = horner.horner_scheme(coeff, stopien, x1)

                 xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))

                 x0 = x1
                 x1 = xi

                 print(f"The root was found to be at {xi}")






