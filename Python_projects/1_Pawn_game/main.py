import random
lokalizacjaPionka = 0
iloscHetmanow = 5

plansza = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]

def losowanie_pionka():
    global lokalizacjaPionka
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    if ((plansza[a][b]) == '[ ]'):
        plansza[a][b] = '[P]'
        lokalizacjaPionka = a,b
    else:
        losowanie_pionka()

def losowanie_hetmana():
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    if((plansza[a][b])=='[ ]'):
        plansza[a][b] = '[H]'
    else:
        losowanie_hetmana()

def sprawdzanie_bicia():
    pozycjeBijacychHetmanow = []
    a = lokalizacjaPionka[0]
    b = lokalizacjaPionka[1]

    while(b>-1): #sprawdza w lewo
        if(plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            b = b-1
    b = lokalizacjaPionka[1]
    while(b<8): #sprawdza w prawo
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            b = b+1
    b = lokalizacjaPionka[1]
    while (a > -1):  # sprawdza w gore
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a - 1
    a = lokalizacjaPionka[0]
    while (a < 8):  # sprawdza w dol
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a + 1
    a = lokalizacjaPionka[0]
    while (b>-1 and a > -1):  # sprawdza skos gora/lewo
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a - 1
            b = b - 1
    a = lokalizacjaPionka[0]
    b = lokalizacjaPionka[1]
    while (b < 8 and a > -1):  # sprawdza skos gora/prawo
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a - 1
            b = b + 1
    a = lokalizacjaPionka[0]
    b = lokalizacjaPionka[1]
    while (b < 8 and a < 8):  # sprawdza skos dol/prawo
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a + 1
            b = b + 1
    a = lokalizacjaPionka[0]
    b = lokalizacjaPionka[1]
    while (b > - 1 and a < 8):  # sprawdza skos dol/lewo
        if (plansza[a][b]) == '[H]':
            pozycjeBijacychHetmanow.append([a,b])
            break
        else:
            a = a + 1
            b = b - 1
    a = lokalizacjaPionka[0]
    b = lokalizacjaPionka[1]

    if (len(pozycjeBijacychHetmanow)>0):
        print('Pionek zostanie zbity przez Hetmanow na polach: ')
        for pole in pozycjeBijacychHetmanow:
            print(pole)
    elif(len(pozycjeBijacychHetmanow)==0):
        print('Pionek nie zostanie zbity')

def wyswietl_plansze():
    print('   0 ', ' 1 ', ' 2 ',' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ')
    liczba = 0
    for linia in plansza:

        print(liczba, linia[0],linia[1],linia[2],linia[3],linia[4],linia[5],linia[6],linia[7])
        liczba = liczba+1
    sprawdzanie_bicia()

def dodatkowe_funkcje():
    wybor = int(input('''Co chcesz zrobić?
    1 - Wylosuj nowe pole dla pionka
    2 - Usun dowolnego Hetmana
     '''))
    if (wybor == 1):
        plansza[lokalizacjaPionka[0]][lokalizacjaPionka[1]] = '[ ]'
        losowanie_pionka()
    elif (wybor == 2):
        a = int(input('Podaj szereg Hetmana, ktorego chcesz usunac: '))
        b = int(input('Podaj rząd Hetmana, ktorego chcesz usunac: '))

        if(plansza[a][b] == '[H]'):
            plansza[a][b] = '[ ]'
        else:
            print('Na podanym polu nie ma Hetmana!')
    else:
        print('Nie ma takiego wyboru!')
    wyswietl_plansze()
    dodatkowe_funkcje()

losowanie_pionka()
for x in range(iloscHetmanow):
    losowanie_hetmana()
wyswietl_plansze()
dodatkowe_funkcje()