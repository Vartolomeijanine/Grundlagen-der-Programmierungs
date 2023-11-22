from A3_Paket.logik import S_S_P_Reset

def S_S_P_Drawings(x):

    inside = False
    l = []
    
    if x == "Schere":
        #Prints out the drawing for scissors

        with open ("S_S_P_Zeichnungen.txt") as f:
            for line in f:
                line = line.rstrip()

                if line.startswith("---"):
                    inside = True
                
                elif line.startswith("###"):
                    inside = False
                
                elif inside:
                    l.append(line)

    elif x == "Stein":
        #Prints out the drawing for stone
        
        with open ("S_S_P_Zeichnungen.txt") as f:
            for line in f:
                line = line.rstrip()
                
                if line.startswith("###"):
                    inside = True
                
                elif line.startswith("$$$"):
                    inside = False
                
                elif inside:
                    l.append(line)

    elif x == "Papier":
        #Prints out the drawing for paper

        with open ("S_S_P_Zeichnungen.txt") as f:
            for line in f:
                line = line.rstrip()

                if line.startswith("$$$"):
                    inside = True
                
                elif line.startswith("((("):
                    inside = False
                
                elif inside:
                    l.append(line)
    
    result = '\n'.join(l)
    return result


def Ergebnis_spiel(human_score, computer_score):
    
    l = []
    l.append("Ergebnis ist" + " " + str(human_score) + " " + "-" + " " + str(computer_score) + '\n')
    l.append("Was möchtest du spielen?")
    
    result = "\n".join(l)
    return result


def win_check(win):
    
    if win == 0:
        return "Niemand gewinnt die Runde\n"
    elif win == 1:
        return "Der Mensch gewinnt die Runde\n"
    elif win == 2:
        return "Die Rechner gewinnt die Runde\n"
    
    
def game_win(human_score):
    
    if human_score == 2:
        return "Der Mensch gewinnt das Spiel"
    else:
        return "Die Rechner gewinnt das Spiel"
    
    
def game_remake(remake, human_score, computer_score):
    
    if remake == "Ja":
        S_S_P_Reset(human_score, computer_score)
        return "Spiel weiter!"
    else:
        return "Spiel beendet. Vielen Dank!"