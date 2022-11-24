x = 1
warunek = True
while warunek:
    print(f"{x}")
    while x >= 5 and x%5==0:
        print("duża liczba!")
        break
    x+=1
    if x > 25:
        break
    pass
