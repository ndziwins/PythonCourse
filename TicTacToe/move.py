def ruch(plansza, gracz, kolumna, wiersz):
    if kolumna > 2 or wiersz > 2 or plansza[wiersz][kolumna] != '[ ]':
        print("Błędny ruch. Spróbuj ponownie.")
        return gracz
    plansza[wiersz][kolumna] = f'[{gracz}]'
    gracz = zmianaGracza(gracz)
    return gracz

def zmianaGracza(gracz):
    if gracz == 'X':
        gracz = 'O'
    elif gracz =='O':
        gracz = 'X'
    return gracz

def czyKoniec(plansza):
    if plansza[0][0] != "[ ]" and plansza[0][0] == plansza[0][1] and plansza[0][1] == plansza[0][2]:
        return True
    elif plansza[1][0] != "[ ]" and plansza[1][0] == plansza[1][1] and plansza[1][1] == plansza[1][2]:
        return True
    elif plansza[2][0] != "[ ]" and plansza[2][0] == plansza[2][1] and plansza[2][1] == plansza[2][2]:
        return True
    elif plansza[0][0] != "[ ]" and plansza[0][0] == plansza[1][0] and plansza[1][0] == plansza[2][0]:
        return True
    elif plansza[0][1] != "[ ]" and plansza[0][1] == plansza[1][1] and plansza[1][1] == plansza[2][1]:
        return True
    elif plansza[0][2] != "[ ]" and plansza[0][2] == plansza[1][2] and plansza[1][2] == plansza[2][2]:
        return True
    elif plansza[0][0] != "[ ]" and plansza[0][0] == plansza[1][1] and plansza[1][1] == plansza[2][2]:
        return True
    elif plansza[0][2] != "[ ]" and plansza[0][2] == plansza[1][1] and plansza[1][1] == plansza[2][0]:
        return True
    else:
        return False