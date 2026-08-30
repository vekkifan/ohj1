import random
arpa = int(input("anna arpakuutioiden määrä: "))

summa = 0

for i in range(arpa):
    luku = random.randint(1, 6)
    summa += luku

print(summa)
