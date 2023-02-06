'''
Cuenta si la primera letra de una palabra es match de la letra del usuario
'''

palabras=[]
c = 0

for i in range (0,5):
    palabras.append(str(input()))


letra = str(input())
for j in palabras:
    f = j.strip()
    if f[0].lower() == letra.lower():
        c += 1

print(c)