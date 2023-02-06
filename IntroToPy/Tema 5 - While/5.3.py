'''
Dependiendo de la clave, suma los números.
'''


Clave = str(input())
Total = 0

while Clave != "X":
    if Clave == "A":
        Precio = 120
        Total = Total + Precio
        print(Precio)
        Clave = str(input())
    elif Clave == "B":
        Precio = 250
        Total = Total + Precio
        print (Precio)
        Clave = str(input())
    elif Clave == "C":
        Precio = 360
        Total = Total + Precio
        print (Precio)
        Clave = str(input())

print(Total)
