from A1_Paket.menu import menu_a1
from A2_Paket.menu import menu_a2
from A3_Paket.menu import menu_a3


def main():
    while True:

        try:

            aufgabe = int(input("Welches Aufgabe wählst du? (1, 2 oder 3; 0, um das Programm zu beenden): "))

        except ValueError:

            return
        """
        Integer-Eingabe erwartet
        Programm beendet
        """

        if not (aufgabe == 0 or aufgabe == 1 or aufgabe == 2 or aufgabe == 3):
            return "Wert unmöglich. Beendetes Programm"

        if not aufgabe:
            return "Beendetes Programm"

        elif aufgabe == 1:

            print(menu_a1())

        elif aufgabe == 2:

            print(menu_a2())

        elif aufgabe == 3:

            print(menu_a3())


main()