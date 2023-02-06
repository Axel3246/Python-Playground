#Realiza un programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.

x = int(input())
y = int(input())
z = int(input())

if (x > z) and (x > y):
    print (x)
elif (y > z) and (y > z):
    print (y)
else:
    print (z)