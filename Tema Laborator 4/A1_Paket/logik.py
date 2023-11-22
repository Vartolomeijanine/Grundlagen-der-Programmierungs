def w_move(pen):
    pen.forward(10)
    
def s_move(pen):
    pen.backward(10)
    
def a_move(pen):
    pen.left(45)
    
def d_move(pen):
    pen.right(45)
    
def f_up(pen):
    pen.penup()
    
def g_down(pen):
    pen.pendown()
    
    
def draw_letter(dictionar, text, pen):
    
    for i in range(len(text)):
        letter = text[i]
            
        if letter in dictionar:
            
            value = dictionar.get(letter)
            
            for j in range(len(value)):
                
                if value[j] == 'w':
                    w_move(pen)
                    
                elif value[j] == 's':
                    s_move(pen)
                    
                elif value[j] == 'a':
                    a_move(pen)
                    
                elif value[j] == 'd':
                    d_move(pen)
                    
                elif value[j] == 'f':
                    f_up(pen)
                
                elif value[j] == 'g':
                    g_down(pen)
            
        else:
            pen.reset()
            return "Dieses Symbol existiert nicht im Wörterbuch"
    return ""
     
     

def make_string(symbol_input, pen):
    
    if symbol_input == 'w':
        w_move(pen)
        return 1
                    
    elif symbol_input == 's':
        s_move(pen)
        return 1
                    
    elif symbol_input == 'a':
        a_move(pen)
        return 1
                    
    elif symbol_input == 'd':
        d_move(pen)
        return 1
                    
    elif symbol_input == 'f':
        f_up(pen)
        return 1
                
    elif symbol_input == 'g':
        g_down(pen)
        return 1
    
    elif symbol_input == '':
        return 1
        
    else:
        return 0



def key_check(symbol, dictionar):

    if symbol in dictionar.keys():
        return 0
    return 1



def symbol_check(symbol_input, dictionar):

    if symbol_input in dictionar.values():
            return 0
    return 1



def nehme_Symbolen(dictionar):
    
    try:
        with open("Symbolen.txt", 'r') as f:
            for line in f:
                l = []
                l = line.split()
                v1 = key_check(l[0], dictionar)
                v2 = symbol_check(l[1], dictionar)
            
                if v1 and v2:
                    dictionar[l[0]] = l[1]
                    
        return "Alle Symbole von Symbolen.txt sind untergeladen"
                    
    except IndexError:
        
        return "Es gibt keine Symbolen in der Symbolen.txt Datei"
        
        

def Symbol_bauen():
    
    ok = 0
    while not ok:

        symbol = input("Schreib ein einziges Charakter Name für dein Symbol: ")
        
        if not len(symbol) == 1:
            
            print("Symbol nicht akzeptiert. Schreib nur ein einziges Charakter")
            
        else:
            
            ok = 1
            
    return symbol
                


def Symbol_input_bauen(pen):
    
    ok = 0
    l = ""
    while not ok:

        symbol_input = input("Schreib die Anweisungen für dein Symbol: ")
        
        if make_string(symbol_input, pen):
            l += symbol_input
            
        else:
            
            print("Befehle zurückgebracht")
            l = ""
            pen.reset()
            
        if symbol_input == "" and l != "":
            ok = 1
            
    return l



def key_symbol_pass(key_pass, symbol_pass, symbol, symbol_input):
    
    if  (key_pass == 0 or symbol_pass == 0):
        
        l = []
        l.append("Die Folgende Sachen sind schon im Symbol-Wörterbuch:")
        
        if not key_pass:
            l.append("Symbol")
            
        if not symbol_pass:
            l.append("Symbol Anweisungen")
            
        l.append("Symbol Aufbau gestoppt")
        result = '\n'.join(l)
        
        return result
                            
    else:
                            
        save = input("Möchtest du dieses Symbol speichern? (Ja für ja, oder was anderes für nein): ")
        
        if save == "Ja":
            
            with open("../Symbolen.txt", 'a') as f:
                f.write(symbol)
                f.write(" ")
                f.write(symbol_input)
                f.write("\n")
            return "Symbol gespeichert"
        
        return "Symbol nicht geschpeichert"
