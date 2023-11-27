def replace_word(text, change_word, changed_word, count):
    
    l = text.split()
    for i in range(len(l)):
        if change_word in l[i]: #daca gaseste cuvantul pisica
            l[i] = l[i].replace(change_word, changed_word) #se schimba pisica in caine
            count += 1
    text = ' '.join(l) #se concateneaya cuvintele cu un spatiu intre fiecare
    return text, count
