from A2_Paket.logik import *
from A2_Paket.console import *

def menu_a2():
    
    name = input("Mit welchem Datei möchtest du arbeiten?: ")
    text = None
    text = read_from_file(name, text)
    
    if text == "Datei existiert nicht":
        return "Datei existiert nicht"
            
    change_word = input("Welches Wort möchtest du ersetzen?: ")
    changed_word = input("Mit welchem Wort möchtest du das ersetzen?: ")
    count = 0
            
    text, count = replace_word(text, change_word, changed_word, count)
    write_in_file(name, text)
            
    return file_result(change_word, changed_word, count)
