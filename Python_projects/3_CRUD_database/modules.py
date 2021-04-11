import datetime
from prettytable import PrettyTable
date = datetime.datetime.now().year

def check_pesel(pesel):
    pesel = str(pesel)
    dataUrodzenia = 0
    plec = 0
    if (len(pesel) != 11):
        print('Pesel nie ma 11 cyfr')
        return 'zly'
    else:
        if(int(pesel[0:1])<3):
            dataUrodzenia = f'20{pesel[0:2]}'
        else:
            dataUrodzenia = f'19{pesel[0:2]}'
    wiek = int(date) - int(dataUrodzenia)
    if (int(pesel[9])%2==0):
        plec = 'k' 
    else:
        plec = 'm'
    return wiek, plec


def load_file(lista):
    try:
        f = open("dane.txt", "r")
        lines = f.readlines()
        users = []
        for user in lines:
            user = user.split(";")
            find = False
            for osoba in lista:
                if (osoba[0]==user[0]):
                    print('Id', user[0],  'już istnieje, użytkownik', user[1], user[2], user[3], 'nie został dodany')
                    find = True
                    break
            if (find == False):
                user[3]=str(user[3]).replace("\n", "")
                lista.append(user)
        print("Dane zostały wczytane z pliku!")
        return lista
        
    finally:
        f.close()

def edit_person(lista):
    klucz = False
    wybor = input("Podaj id osoby, którą chcesz edytować: ")
    for osoba in lista:
        if osoba[0]==wybor:
            wybor2 = input("""Co chesz zmienic?
1 - Imię  |  2 - Nazwisko  |  3 - Pesel
Wybór: """)
            if (wybor2 == '1'):
                newName = input('Podaj nowe imię: ')
                osoba[1] = newName
            elif(wybor2 == '2'):
                newSurname = input('Podaj nowe nazwisko: ')
                osoba[2] = newSurname
            elif(wybor2 == '3'):
                newPesel = input('Podaj nowy pesel: ')
                if(check_pesel(newPesel) == 'zly'):
                    print("Podany pesel jest błędny")
                    return lista
                osoba[3] = newPesel
            print('Dane zostały zmienone!')
            klucz = True
    if(klucz == False):
        print('Brak takiego ID!')
    return lista

def delete_person(lista):
    wybor = input("Podaj id osoby, którą chcesz usunąć: ")
    klucz = False
    for osoba in lista:
        if osoba[0]==wybor:
            lista.remove(osoba)
            klucz = True
            print('Dane zostały usuniete!')
    if(klucz==False):
        print('Brak takiego ID!')
    return lista


def add_person(lista):
    nowaOsoba = []
    newId = input("Podaj ID: ")
    try:
        newId = int(newId)
    except:
        print("Błędny ID")
        return lista
    newId = str(newId)
    for osoba in lista:
        if(newId == osoba[0]):
            print("ID już istnieje")
            return lista
    newName = input("Podaj Imię: ")
    newSurname = input("Podaj Nazwisko: ")
    newPesel = input("Podaj Pesel: ")
    if(check_pesel(newPesel) == 'zly'):
        print("Podany pesel jest błędny")
        return lista
    nowaOsoba = [newId, newName, newSurname, newPesel]
    print(nowaOsoba)
    lista.append(nowaOsoba)
    print('Dane zostały dodane!')
    return lista

def save_file(dane):
    try:
        f = open("dane.txt", "w")
        for osoba in dane:
            osoba = str(osoba).replace("', '", ";").replace("['", "").replace("']", "\n")
            f.write(osoba)
        print('Dane zostały zapisane do pliku!')
    finally:
        f.close()

def wyswietl(dane):
    dane.sort(key=lambda elem: int(elem[0]))
    sredniWiek = 0
    kobiety = 0
    mezczyzni = 0
    myTable = PrettyTable(["ID", "IMIE", "NAZWISKO", "PESEL"])
    for osoba in dane:
        myTable.add_row([osoba[0], osoba[1], osoba[2], osoba[3]])
        danePesel = check_pesel(osoba[3])
        sredniWiek = sredniWiek + int(danePesel[0])
        if (danePesel[1]=='k'):
            kobiety = kobiety+1
        elif (danePesel[1]=='m'):
            mezczyzni = mezczyzni+1
    print(myTable)
    if(len(dane)>0): 
        print('Śr.wiek:', round(int(sredniWiek)/len(dane), 1), '|', ' Kobiet:', kobiety, '|', 'Meżczyźni:', mezczyzni)
        print('---------------------------------------')
    wybor = input("""1 - Dodaj osobę      4 - Wczytaj z pliku
2 - Edytuj osobę     5 - Zapisz do pliku
3 - Usuń osobę       6 - Zakończ program
Wybór: """)
    if(wybor == '1'):
        wczytane = add_person(dane)
    elif(wybor == '2'):
        wczytane = edit_person(dane)
    elif(wybor == '3'):
        wczytane = delete_person(dane)
    elif(wybor == '4'):
        wczytane = load_file(dane)
    elif(wybor == '5'):
        save_file(dane)
    elif(wybor == '6'):
        print("Program zakończony")
        return 0
    wyswietl(dane)