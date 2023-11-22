def write_in_file(name, text):
    
    with open(name, 'w') as a:
        a.write(text)
        
def read_from_file(name, text):
    
    try:
        with open(name, 'r') as a:
            return a.read()

            
    except FileNotFoundError:
        return "Datei existiert nicht"
        
def file_result(change_word, changed_word, count):
    
    if count == 0:
        return "Dieses Wort gibt nicht. Nichts war verändert."
    else:
        return change_word + " " + "war mit" + " " + changed_word + " " + "an" + " " + str(count) + " "+ "Stelle ersetzt"
