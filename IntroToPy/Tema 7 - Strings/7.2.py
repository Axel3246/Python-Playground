"""
Diseña el programa que reciba un string y regrese un string construido por los primeros dos
y los últimos dos caracteres del string original. Si la longitud del string que recibe es menor a dos,
debe regresar un string vacío.
"""
string1 = input()

if len(string1) < 2:
    string2 = " "
    print(string2)
else:
    print(string1[0:2], end = ' ')
    print(string1[-2]+string1[-1])


