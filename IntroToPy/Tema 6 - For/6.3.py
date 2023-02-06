'''
Imprime la cuenta hasta i, luego la cuenta regresiva
'''


i = int(input())


for final in range (1, i):
    print(final, end=", ")

for final in range (i, 1, -1):
    print(final, end=(", "))

print (1)


