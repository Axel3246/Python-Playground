#Escribe un programa que calcule el IMC (Indice de Masa Corporal) de una persona,
#el cual se utiliza para determinar si la proporción de peso y altura es adecuada.

peso = float(input())
altura = float(input())

#Proceso y Salidas

indice = peso/(altura**2)

if indice < 20:
    print ("PESO BAJO")
elif (20 <= indice < 25):
    print ("NORMAL")
elif (25 <= indice < 30):
    print ("SOBREPESO")
elif (30 <= indice <40):
    print ("OBESIDAD")
elif (40 <= indice):
    print ("OBESIDAD MORBIDA")
                               
                               
