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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    polttomoottoriauto.kiihdyta(110)

    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauto ({sahkoauto.rekisteritunnus}):")
    print(f"  - Huippunopeus: {sahkoauto.huippunopeus} km/h")
    print(f"  - Akkukapasiteetti: {sahkoauto.akkukapasiteetti} kWh")
    print(f"  - Kuljettu matka 3 tunnin jälkeen: {sahkoauto.kuljettu_matka} km\n")

    print(f"Polttomoottoriauto ({polttomoottoriauto.rekisteritunnus}):")
    print(f"  - Huippunopeus: {polttomoottoriauto.huippunopeus} km/h")
    print(f"  - Bensatankin koko: {polttomoottoriauto.bensatankin_koko} l")
    print(f"  - Kuljettu matka 3 tunnin jälkeen: {polttomoottoriauto.kuljettu_matka} km")
