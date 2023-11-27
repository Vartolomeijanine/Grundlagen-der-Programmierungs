from A3_Paket.logik import S_S_P_Reset


def read_from_file(choice): #citeste si afiseaza desenele cu optiunile alese din fisierele respective
    try:
        if choice == "Stein":
            file = open("stein.txt", "r")
            content = file.read()
            if content:
                print(content)
            else:
                print("Die Datei ist leer.")
            file.close()
        elif choice == "Papier":
            file = open("papier.txt", "r")
            content = file.read()
            if content:
                print(content)
            else:
                print("Die Datei ist leer.")
            file.close()
        elif choice == "Schere":
            file = open("schere.txt", "r")
            content = file.read()
            if content:
                print(content)
            else:
                print("Die Datei ist leer.")
            file.close()

    except FileNotFoundError:
            print("Zeichnungsdatei nicht gefunden.")

def Ergebnis_spiel(human_score, computer_score): # iti spune scorul actual
    
    l = []
    l.append("Ergebnis ist" + " " + str(human_score) + " " + "-" + " " + str(computer_score) + '\n')
    l.append("Was möchtest du spielen?")

    result = "\n".join(l)
    return result


def win_check(win): # vede cine a castigat runda si afiseaza mesajul corespunzator
    
    if win == 0:
        return "Niemand gewinnt die Runde\n"
    elif win == 1:
        return "Der Mensch gewinnt die Runde\n"
    elif win == 2:
        return "Die Rechner gewinnt die Runde\n"
    
    
def game_win(human_score): #daca cineva castiga 2 runde consecutive castiga jocul
    
    if human_score == 2:
        return "Der Mensch gewinnt das Spiel"
    else:
        return "Die Rechner gewinnt das Spiel"

    
def game_remake(remake, human_score, computer_score): #reseteaza scorul daca mai vrei sa joci inca o dats
    
    if remake == "Ja":
        S_S_P_Reset(human_score, computer_score)
        return "Spiel weiter!"
    else:
        return "Spiel beendet. Vielen Dank!"