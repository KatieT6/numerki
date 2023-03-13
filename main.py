# This is a sample Python script.
from email.policy import default

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("1. Wielommianowa")
print("2. Trygonometryczna")
print("3. Wykladnicza")


def przedzial_poszukiwania():
    print("Okresl przedział: \n Od:")


user_input = int(input("Wybierz jedna z funkcji:"))

match user_input:
    case 1:
        print("Wielommianowa")
        przedzial_poszukiwania()

    case 2:
        print("Trygonometryczna")

    case 3:
        print("Wykladnicza")
