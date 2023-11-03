#2.a
def generate_firstnPrime(n):
    for number in range(2, n + 1): # am pus +1 pentru ca el merge pana la strict n + 1. daca puneam n, mergea pana la n-1
        if number == 2: #primul nr prim si singurul nr prim par
            print ('2')
        elif number % 2 != 0: #daca nr e impar
            ok = True # presupunem ca number e prim
            for d in range (3, number // 2, 2): #merge din 2 in 2 de la 3 pana la jumatatea lui n( // - impartire intreaga
                if number % d == 0: # daca are divizori, presupunerea ca e prim e falsa
                    ok = False
            if ok == True: # daca e prim il afisam
                print(number)


value = int(input('n = ')) # imi apare pe ecran n= iar eu tastez un nr n, iar functia se va apela
generate_firstnPrime(value)

#2.b

#11.a
def primeIntreEle(nr1, nr2): #euclid
    if nr1>nr2:
        nr1,nr2 = nr2,nr1 #interschimbat
    while nr2 != 0:
        rest = nr1 % nr2
        nr1 = nr2
        nr2 = rest
    if nr1 == 1:
        return True
    else:
        return False

def parcurgere(list):
    count = 0
    maxSecv = -1
    result = []
    temp = []
    for number in range(0, len(list) - 1):
        if primeIntreEle(list[number], list[number + 1]) == True and count == 0:
            temp = []
            temp.append(list[number])
            temp.append(list[number + 1])
            count = 2
        elif primeIntreEle(list[number], list[number + 1]) == True and count >= 2:
            ok = True
            for nr in range(0, len(temp)):
                if primeIntreEle(temp[nr], list[number + 1]) == False:
                    ok = False
                    count = 0
            if ok == True:
                temp.append(list[number + 1])
                count = count + 1
        else:
            count = 0
        if count > maxSecv:
            maxSecv = count
            result = temp
    return result


#11.b
def citireLista():
    list = input('Introdu lista: ')
    list = list.split() # noi intrroducem niste nr dar calculatorul le separa si le pune in lista


def strictDesc(list):
    temp = [] #lista in care stochez numerele
    count = 0 #contor
    maxSecv = - 1
    for number in range(0, len(list) - 1): # pt ca numaratoarea incepe de la 0 trebuie sa pun len(list)-1
        if count == 0 and list[number] > list[number + 1]:
            temp = []
            count = 2
            temp.append(list[number]) # punem la sfarsit nr
            temp.append(list[number + 1])
        elif count >= 2 and list[number] > list[number + 1]:
            count = count + 1
            temp.append(list[number + 1])
        else:
            count = 0
        if count > maxSecv:
            maxSecv = count
            result = temp

    return result

citireLista()
strictDesc(list)