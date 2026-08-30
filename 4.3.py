luvut = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break

    luvut.append(int(luku))

print(f"Pienin luku: {min(luvut)}")
print(f"Suurin luku: {max(luvut)}")
