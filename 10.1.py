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
        """Siirtää hissin haluttuun kerrokseen kutsumalla kerros_ylös- tai kerros_alas-metodia."""
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print(f"Virhe: Kerros {kohdekerros} on hissin toiminta-alueen ulkopuolella ({self.alin_kerros}-{self.ylin_kerros}).")
            return

        # Siirretään hissiä ylöspäin, kunnes ollaan kohdekerroksessa
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()

        # Siirretään hissiä alaspäin, kunnes ollaan kohdekerroksessa
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


# Pääohjelma testausta varten
if __name__ == "__main__":
    # Luodaan hissi, jonka alin kerros on 1 ja ylin kerros 7
    h = Hissi(1, 7)

    print("--- Siirrytään haluttuun kerrokseen (5) ---")
    h.siirry_kerrokseen(5)

    print("\n--- Siirrytään takaisin alimpaan kerrokseen ---")
    h.siirry_kerrokseen(1)
