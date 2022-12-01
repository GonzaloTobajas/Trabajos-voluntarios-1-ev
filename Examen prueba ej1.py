p1=input("Dime una palabra--> ")
lista=p1.split(",")
for palabra in lista:
    cons=0
    print(" ")
    if len(palabra)>=10:
        print("Tiene más de 10 letras")
    for cont in range(0,len(palabra)):
        letra=palabra[cont]
        if letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u":
            cons=cons+1
            print(letra)
        else:
            letra="*"
            print(letra)
    print(cons)