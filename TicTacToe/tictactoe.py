'''
0 - puste pole
1 - oznacza gracz x
2 - oznacza gracz o
'''

from board import *
from move import *

gracz = 'X'
czyKoniecGry = False

plansza = tworzPlansze()
printPlansza(plansza, gracz)

kolumna = 0
wiersz = 2
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)

kolumna = 0
wiersz = 1
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)

kolumna = 1
wiersz = 1
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)

kolumna = 1
wiersz = 1
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)

kolumna = 1
wiersz = 0
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)

kolumna = 4
wiersz = 1
gracz = ruch(plansza, gracz, kolumna, wiersz)
printPlansza(plansza, gracz)