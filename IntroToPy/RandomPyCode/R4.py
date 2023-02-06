# Escribe un programa que dada una fecha (año, mes y día), devuelva la fecha del día siguiente.

año = int(input('¿Cuál es el año? '))

while(año < 0):
    año = int(input('Da un año correcto '))
    
mes = int(input('¿Cuál es el mes? '))

while(mes < 1 or mes > 12):
    mes = int(input('Da un mes correcto '))
    
dia = int(input('¿Cuál es el día? '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
    if dia > 0 and dia < 31:
        dia = dia + 1
    else:
        mes = mes + 1
        dia = 1

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia < 30:
        dia = dia + 1
    else:
        mes = mes + 1
        dia = 1

if mes == 2:
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        if dia > 0 and dia < 30:
            dia = dia + 1
        else:
            mes = mes + 1
            dia = 1
    else:
        if dia > 0 and dia < 29:
            dia = dia + 1
        else:
            mes = mes + 1
            dia = 1

elif mes == 12:
    if dia > 0 and dia < 31:
        dia = dia + 1
    else:
        año = año + 1
        mes = 1
        dia = 1

print('Año:', año)
print('Mes:', mes)
print('Día:', dia)
