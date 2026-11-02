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


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        """Arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia."""
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        """Tulostaa kaikkien autojen sen hetkiset tiedot selkeänä taulukkona."""
        print(f"\n{'Rekisteritunnus':<15} | {'Huippunopeus (km/h)':<20} | {'Nykyinen nopeus (km/h)':<22} | {'Kuljettu matka (km)':<20}")
        print("-" * 85)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<20} | {auto.tamanhetkinen_nopeus:<22} | {auto.kuljettu_matka:<20.1f}")

    def kilpailu_ohi(self):
        """Palauttaa True, jos jokin autoista on ajanut vähintään kilpailun kokonaiskilometrimäärän."""
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippunopeus))

    romuralli = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0

    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            print(f"\n--- Tilanne {tunnit} tunnin jälkeen ---")
            romuralli.tulosta_tilanne()

    print(f"\n=== KILPAILU PÄÄTTYI! Voittaja on selvillä {tunnit} tunnin ajon jälkeen. ===")
    print(f"Kilpailu: {romuralli.nimi}")
    romuralli.tulosta_tilanne()
