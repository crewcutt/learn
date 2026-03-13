def ferma (a, b, c, n):
#    print((a ** n) + (b ** n)); print((c ** n))
    if (a ** n) + (b ** n) == (c ** n):
        print("Ферма ошибся")
    else:
        print("это не работает")

a = 3; b = 4; c = 5; n = 3
ferma (a, b, c, n)
a = 7; b = 3; c = 10; n = 4
ferma (a, b, c, n)
a = 5; b = 4; c = 9; n = 3
ferma (a, b, c, n)
