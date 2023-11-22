def replace_word(text, change_word, changed_word, count):
    
    l = text.split()
    for i in range(len(l)):
        if change_word in l[i]:
            l[i] = l[i].replace(change_word, changed_word)
            count += 1
    text = ' '.join(l)
    return text, count
