#El código lee un número y cuenta los valores anteriores a ese numero y los multipiplica por su cuadrado

n = int(input())

for n in range (0,n):
    cuadrado = n ** 2
    print (cuadrado)
    n = n - 1