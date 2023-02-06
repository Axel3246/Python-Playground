'''
Da la suma 2+2 = 4, por ejemplo, de los números deseados
poniendolos como una lista
'''

n = int(input())
list = []
suma = 0

while n <= 0:
    print("No funciona tu valor")
    n = int(input())
else:
    print("Aceptado")
    for i in range (0,n):
        num = int(input())
        print("lista[" + str(i) + "] ="+ " " + str((num)))
        suma = suma + num
    print(n)
    print(suma)
    print((suma/n))