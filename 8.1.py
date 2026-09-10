import csv

icao = input("Anna lentoaseman ICAO-koodi: ")

with open("airports.csv", encoding="utf-8") as tiedosto:
    lukija = csv.DictReader(tiedosto)

    for rivi in lukija:
        if rivi["ident"] == icao:
            print(rivi["name"])
            print(rivi["municipality"])
            break
