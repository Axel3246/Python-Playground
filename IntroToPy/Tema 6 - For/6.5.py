'''
Da una cantidad y la multiplica por un interés anual
'''


cantidad = float(input())
ianual = int(input())

if (cantidad<=0) or (ianual<=0):
    print("Error en los datos")
else:
    mensual = ianual/12/100
    for i in range (1, 13, 1):
        cantidad = cantidad * (1+mensual)
    
    print(round(cantidad,2))
