from A3_Paket.logik import *
from A3_Paket.console import *
import random

def menu_a3():
    
    while True:
                
        print("Willkommen zu Schere, Stein, Papier!")
        human_score = 0
        computer_score = 0
        S_S_P_list = ["Schere", "Stein", "Papier"]
                
        while human_score != 2 and computer_score != 2:
                    
            computer_choice = random.choice(S_S_P_list)
            print(Ergebnis_spiel(human_score, computer_score))
                    
            human_choice = input("Schreib hier: ")
                    
            if not (human_choice == "Schere" or human_choice == "Stein" or human_choice == "Papier"):
                return "Nur gegebene Wörter erlaubt"

            print("Rechner spielt:", computer_choice)
            print(S_S_P_Drawings(computer_choice))
            print("Mensch spielt:", human_choice)
            print(S_S_P_Drawings(human_choice))
                    
            win = S_S_P_Cases(human_choice, computer_choice)
                    
            print(win_check(win))
                    
            if win == 1: human_score += 1
            elif win == 2: computer_score += 1 
                    
        print(game_win(human_score))
                
        remake = input("Möchtest du nochmal spielen? (Ja oder was anderes wenn nein): ")
                
        remake = game_remake(remake, human_score, computer_score)
        if remake != "Spiel weiter!": return remake
        else: print("Spiel weiter!")
