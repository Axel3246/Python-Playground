#Escribe un programa en Python que lea la edad de una persona y si tiene (s/n) identificación oficial
#De salida debe mostrar Si si puede obtener su licencia o No si no la puede obtener

edad = int(input())
ID = input()

#Proceso y Salidas

if edad >= 18 and ID == "s":
    print ("Si")
elif (edad >= 18 and ID == "n"):
    print ("No")
elif (edad < 18 and ID == "s"):
    print ("No")
elif (edad < 18 and ID == "n"):
    print ("No")
