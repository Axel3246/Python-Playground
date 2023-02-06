#Determina que tipo de triángulo es

x = int(input())
y = int(input())
z = int(input())

#Proceso

if ((x + y)>z) and ((x + z)>y) and ((y + z)>x) and (x>0) and (y>0) and (z>0):
        if (x == y) and (y == z):
            print ("EQUILATERO")
        elif (((x == y) and (y != z)) or ((x == z) and (y != z)) or ((z == y) and (y != x))):
            print ("ISOSCELES")
        else:
            print ("ESCALENO")
else:
    print ("NO ES TRIANGULO")
            
