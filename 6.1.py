import random

def heita_noppaa():
    return random.randint(1, 6)

tulos = 0
while tulos != 6:
    tulos = heita_noppaa()
    print(tulos)