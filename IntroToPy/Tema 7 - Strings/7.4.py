"""
Crea un programa que pueda aceptar dos cadenas como entrada e imprima la cadena
con la longitud máxima en la consola. Si dos cadenas tienen la misma longitud,
la función debe imprimir ambas cadenas línea por línea.
"""
str1 = input()
str2 = input()

if len(str1) > len(str2):
    print(str1)
elif len(str1) < len(str2):
    print(str2)
else:
    print(str1)
    print(str2)