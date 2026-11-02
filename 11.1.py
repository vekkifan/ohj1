class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan julkaisut annettujen tietojen mukaisesti
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # Tulostetaan molempien julkaisujen tiedot
    print("--- Lehden tiedot ---")
    aku_ankka.tulosta_tiedot()

    print("\n--- Kirjan tiedot ---")
    hytti_no_6.tulosta_tiedot()
