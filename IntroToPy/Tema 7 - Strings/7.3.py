"""
Escribir un programa en Python que lea un string y muestre como salida el string recibido escrito en reversa,
comenzando con el último carácter y terminando con el primer carácter del string original, y completamente en mayúsculas.
"""

string = input()
print(string.upper()[::-1])