while True:
    tuuma = int(input("Anna tuumamäärä: "))
    num = tuuma * 2.54
    print(num)
    if tuuma <=0:
        print("Negatiivinen numero")
        break
