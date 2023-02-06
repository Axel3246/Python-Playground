'''
Numeros al cuadrado
'''

number =int(input())
normal = []
cuadrado = []

for i in range (number):
        normal.append(int(input()))

print(normal)

for n in normal:
    cuadrado.append(n**2)

print(cuadrado)