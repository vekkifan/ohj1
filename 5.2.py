luvut = []

while True:
    x = input("anna luku: ")
    if x == "":
        break
    luvut.append(int(x))

luvut.sort(reverse=True)

for x in luvut[:5]:
    print(x)
