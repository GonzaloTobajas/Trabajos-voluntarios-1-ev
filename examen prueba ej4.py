palabra=input("Palabra: ")
lista=[]
for cont in range(0,len(palabra)):
    if palabra[cont]=="a" or palabra[cont]=="e" or palabra[cont]=="i" or palabra[cont]=="o" or palabra[cont]=="u" or palabra[cont]=="A" or palabra[cont]=="E" or palabra[cont]=="I" or palabra[cont]=="O" or palabra[cont]=="U":
        if palabra[cont].isupper():
            minu=palabra[cont].lower()
            print(minu)
            lista.append(minu)
        if palabra[cont].islower():
            may=palabra[cont].upper()
            print(may)
            lista.append(may)
    else:
        print(palabra[cont])
        lista.append(palabra[cont])
print(lista[::-1])