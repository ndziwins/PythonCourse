# x = 1
# warunek = True
# while warunek:
#     print(f"{x}")
#     while x >= 5 and x%5==0:
#         print("duża liczba!")
#         break
#     x+=1
#     if x > 25:
#         break

# x = 0
# while x<5:
#     print(f"klocek + {x}")
#     if x == 10:
#         break
#     x+=1
# else:
#     print("koniec while")

lin = input("podaj liczbę liniek: ")
x = 1
while x<=int(lin):
    print('*'*x)
    x+=1

