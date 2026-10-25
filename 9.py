import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara


uusi_auto = Auto("ABC-123", 142)
print(f"Luotu auto: Rekisteritunnus: {uusi_auto.rekisteritunnus}, Huippunopeus: {uusi_auto.huippunopeus} km/h, "
      f}Nykyinen nopeus: {uusi_auto.tamanhetkinen_nopeus} km/h, Kuljettu matka: {uusi_auto.kuljettu_matka} km")

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)
print(f"Nopeus kiihdytysten jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")

uusi_auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")

uusi_auto.tamanhetkinen_nopeus = 60
uusi_auto.kuljettu_matka = 2000
uusi_auto.kulje(1.5)
print(f"Kuljettu matka tunnin 1.5 ajon jälkeen (nopeus 60 km/h): {uusi_auto.kuljettu_matka} km\n")


print(Autokilpailu)

autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippu))

kilpailu_kaynnissa = True
tunnit = 0

while kilpailu_kaynnissa:
    tunnit += 1
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        
        auto.kulje(1)
        
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

print(f"Kilpailu kesti {tunnit} tuntia.\n")

print(f"{'Rekisteritunnus':<15} | {'Huippunopeus (km/h)':<20} | {'Nykyinen nopeus (km/h)':<22} | {'Kuljettu matka (km)':<20}")
print("-" * 85)
for auto in autot:
    print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<20} | {auto.tamanhetkinen_nopeus:<22} | {auto.kuljettu_matka:<20.1f}")
