def gallonat_litroiksi(gallonat):
    return gallonat * 3.78541

while True:
    gallonat = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
    if gallonat < 0:
        break
    print(f"{gallonat} gallonaa on {gallonat_litroiksi(gallonat):.2f} litraa")