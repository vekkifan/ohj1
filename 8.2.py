import csv

maakoodi = input("Anna maakoodi (esim. FI): ").upper()

maatyypit = {}

with open("airports.csv", encoding="utf-8") as tiedosto:
    lukija = csv.DictReader(tiedosto)

    for rivi in lukija:
        if rivi["iso_country"] == maakoodi:
            tyyppi = rivi["type"]

            if tyyppi in maatyypit:
                maatyypit[tyyppi] += 1
            else:
                maatyypit[tyyppi] = 1

if maatyypit:
    print(f"\nLentokentät maassa {maakoodi}:")

    for tyyppi, maara in sorted(maatyypit.items()):
        print(f"{tyyppi}: {maara}")
else:
    print(f"Maakoodilla {maakoodi} ei löytynyt lentokenttiä.")
