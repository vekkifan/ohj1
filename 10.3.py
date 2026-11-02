class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        """Siirtää hissiä yhden kerroksen ylöspäin, jos mahdollista."""
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        """Siirtää hissiä yhden kerroksen alaspäin, jos mahdollista."""
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kohdekerros):
        """Siirtää hissin haluttuun kerrokseen."""
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print(f"Virhe: Kerros {kohdekerros} on hissin toiminta-alueen ulkopuolella ({self.alin_kerros}-{self.ylin_kerros}).")
            return

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        
        # Luodaan haluttu määrä hissejä ja tallennetaan ne listaan
        for _ in range(hissien_lukumäärä):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        """Käskyttää tiettyä talon hissiä siirtymään annettuun kerrokseen."""
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}:")
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)
        else:
            print(f"Virhe: Hissiä numero {hissin_numero} ei löydy talosta.")

    def palohälytys(self):
        """Käskee kaikki talon hissit pohjakerrokseen."""
        print("\n🚨 PALOHÄLYTYS! Kaikki hissit siirretään alimpaan kerrokseen.")
        for i, hissi in enumerate(self.hissit, start=1):
            print(f"\nHissi {i}:")
            hissi.siirry_kerrokseen(self.alin_kerros)


# Pääohjelma
if __name__ == "__main__":
    # Luodaan talo, jonka kerrokset ovat 1-10 ja jossa on 3 hissiä
    talo = Talo(1, 10, 3)

    # Ajetaan talon hissejä eri kerroksiin
    talo.aja_hissiä(1, 5)  
    talo.aja_hissiä(2, 8)  
    talo.aja_hissiä(3, 3)  

    # Simuloidaan palohälytystä
    talo.palohälytys()
