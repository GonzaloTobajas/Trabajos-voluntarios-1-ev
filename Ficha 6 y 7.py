seguir=True
while seguir==True:
    menu=input("SUMA/RESTA/MULTIPLICACION/DIVISION/FIN --> ")
    if menu=="F":
        seguir=False
    else:
        n1=float(input("Dime un número --> "))
        n2=float(input("Dime otro número --> "))
        seguir=True
        if n1==0 or n2==0:
            print("No puedes utiliar el número 0")
        else:
            if menu=="S":
                suma=n1+n2
                print(n1,"más",n2,"es",suma)
            if menu=="R":
                resta=n1-n2
                print(n1,"menos",n2,"es",resta)
            if menu=="M":
                mult=n1*n2
                print(n1,"por",n2,"es",mult)
            if menu=="D":
                div=n1/n2
                print(n1,"entre",n2,"es",div)