import csv
import datetime

frachunki = open("rachunki.csv", newline='', encoding='utf8', errors='ignore')
rachunkidata = list(csv.reader(frachunki, delimiter=';'))
frachunki.close()

def policzwode(wodanew, wodaold, stawka):
    ilezawode = ((wodanew - wodaold) * stawka) - 27.44
    return ilezawode

def policzprad(pradnew, pradold, stawka):
    ileprad=(pradnew-pradold) * stawka
    return ileprad

def obliczrachunki():
    global rachunkidata

    dzis=datetime.datetime.now()
    dzis=dzis.date()

    print("Odczyt z dnia {}".format(str(dzis)))
    wodanew = float(input("Podaj nowy odczyt wody: "))
    wodaold = float(rachunkidata[-1][0])

    ilezawode = policzwode(wodanew, wodaold, 10.34)
    print("Rachunek za wodę: {:.2f}".format(ilezawode))

    newprad1 = float(input("Podaj nowy odczyt pierwszej taryfy: "))
    oldprad1 = float(rachunkidata[-1][1])

    zaprad1 = policzprad(newprad1, oldprad1, 0.6988)
    print("Za prąd 1: {:.2f}".format(zaprad1))

    newprad2 = float(input("Podaj nowy odczyt drugiej taryfy: "))
    oldprad2 = float(rachunkidata[-1][2])

    zaprad2 = policzprad(newprad2, oldprad2, 0.2886)
    print("Za prąd 2: {:.2f}".format(zaprad2))

    zaprad = zaprad1 + zaprad2

    print("\nZa prąd w sumie: {:.2f}".format(zaprad))

    media = ilezawode + zaprad + 150
    print("\nW sumie media: {:.2f}".format(media))

    czynsz = media + 1750

    print("\n\nCzynsz w sumie {:.2f}".format(czynsz))
    nalebka = czynsz / 2
    print("Na łebka {:.2f}".format(nalebka))

    while True:
        zapis = input("Czy chcesz zapisać dane? (y/n)")
        if zapis == 'y':
            rachunkidata.append([wodanew, int(newprad1), int(newprad2), str(dzis)])
            with open("rachunki.csv", "w", newline="", encoding="utf-8") as frachunki:
                writer = csv.writer(frachunki, delimiter = ";")
                writer.writerows(rachunkidata)
            frachunki.close()
            break
        elif zapis == 'n':
            break
        else:
            print("Wybierz prawidłową literę dupo")

def usunostatni():

    global rachunkidata
    del rachunkidata [-1]
    with open("rachunki.csv", "w", newline="", encoding="utf-8") as frachunki:
        writer = csv.writer(frachunki, delimiter = ";")
        writer.writerows(rachunkidata)
    frachunki.close()

def pokazodczyty(dane):
    print("Lp.|      Data      |      Woda     |       Prąd 1      |     Prąd2    ")
    i=0
    for row in dane:
        i+=1
        dataodczytu = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        print("{:<3}|{:>16}|{:>15}|{:>19}|{:>14}".format(i, str(dataodczytu.date()), row[0], row[1], row[2]))
        
#główna pętla programu
while True:
    print("Wybierz opcję:\n")
    print("[o] Podaj odczyty i oblicz opłaty")
    print("[s] Pokaż odczyty")
    print("[d] Usuń ostatni odczyt")
    print("[q] Wyjście")
    wybor = str(input("\nWybierz opcję: "))

    if wybor == 'o':
       obliczrachunki()

    elif wybor == 'd':
        usunostatni()

    elif wybor == 's':
        pokazodczyty(rachunkidata)

    elif wybor == 'q':
        break

    else:
        print("Dupo wybierz prawidłową opcję")


