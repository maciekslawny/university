# FUNKCJA SPRAWDZAJĄCA SILE HASLA

def sprawdzanie_trudnosci(haslo):
    punkty = 0
    ocena = 0
    znakiSpecjalne = ['!','@','#','$','%','^','&','*','(',')', '{', '}', '[', ']', ':', '?', '.']
    cyfry = ['0', '1','2','3','4','5','6','7','8','9']
    polskieZnaki = ['ą','ć','ż','ź','ń','ś','ę','ó']
    for znak in haslo:
        znak = str(znak)
        if (znak in cyfry) or (znak in znakiSpecjalne) or (znak.isupper()) or (znak in polskieZnaki):
            punkty = punkty+2
        else:
            punkty = punkty+1

    if (punkty<8):
        ocena = 'Słabe'
    elif (punkty>7 and punkty<11):
        ocena = 'Średnie'
    elif (punkty>10 and punkty<15):
        ocena = 'Dobre'
    elif (punkty>14):
        ocena = 'Silne'
    print('punkty: ', punkty)
    return ocena

#FUNKCJA SZYFRUJĄCA

def zaszyfruj(slowo):
    kod = ''
    for litera in slowo:
        x = ord(litera)+13
        x = str(x)
        while(len(str(x))<3):
            x = '0' + x
        kod = kod+x

    print('Zaszyfrowane haslo to: ', kod)
    return kod

#FUNKCJA ODSZYFRUJĄCA

def odszyfruj(kod):
    ilosc = int(len(kod))
    odszyfrowaneHaslo = ''
    i = 0
    while(i<ilosc):
        znak = f'{kod[i]}{kod[i+1]}{kod[i+2]}'
        znak = chr(int(znak)-13)
        i = i+3
        odszyfrowaneHaslo = odszyfrowaneHaslo + znak

    print('Odszyfrowane hasło to: ', odszyfrowaneHaslo)

# FUNKCJA DO WPISANIA HASLA

def wpisywanie_hasla():
    slowo = input('Wpisz hasło do oceny: ')
    print('Twoje haslo jest:', sprawdzanie_trudnosci(slowo))
    kod = zaszyfruj(slowo)
    odszyfruj(kod)

wpisywanie_hasla()