from board import *
from move import *

gracz = 'X'
czyKoniecGry = False

plansza = tworzPlansze()
printPlansza(plansza, gracz)

while czyKoniecGry == False :
    kolumna = int(input("Podaj kolumnę do ruchu [0-2]: "))
    wiersz = int(input("Podaj wiersz do ruchu [0-2]: "))
    gracz = ruch(plansza, gracz, kolumna, wiersz)
    printPlansza(plansza, gracz)
    czyKoniecGry = czyKoniec(plansza)
    if czyKoniecGry:
        print("HURRA! Wygrałeś!")
