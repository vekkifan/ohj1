leiv=float(input("leiviskät "))
naul=float(input("naulat "))
luod=float(input("luodit "))


massa=13.3**luod + naul * 13.3 * 32 + leiv * 13.3 * 32 * 20

kg=massa // 1000
g = massa % 1000
print(f"massa: {kg}kg, {g}g ")
