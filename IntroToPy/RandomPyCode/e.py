# Escribe un programa que dada una fecha (año, mes y día), devuelva la fecha del día siguiente.

año = int(input('¿Cuál es el año? '))
mes = int(input('¿Cuál es el mes? '))
dia = int(input('¿Cuál es el día? '))

if ((mes <= 12 and mes >= 1)):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        if mes == 2:
            if dia > 0 and dia < 29:
                dia = dia + 1
            elif dia == 29:
                mes = mes + 1
                dia = 1
            else:
                print('Esa fecha no existe')
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
            if dia > 0 and dia < 31:
                dia = dia + 1
            elif dia == 31:
                mes = mes + 1
                dia = 1
            else:
                print('Esa fecha no existe')

        elif mes == 2:
            if dia > 0 and dia < 28:
                dia = dia + 1
            elif dia == 28:
                mes = mes + 1
                dia = 1
        
         
            if dia > 0 and dia < 30:
                dia = dia + 1
            elif dia == 30:
                mes = mes + 1
                dia = 1
            else:
                print('Esa fecha no existe')
        
        elif mes == 12:
            if dia > 0 and dia < 31:
                dia = dia + 1
            if dia == 31:
                año = año + 1
                mes = 1
                dia = 1
            else:
                print('Esa fecha no existe')
    
    print('Año:', año)
    print('Mes:', mes)
    print('Día:', dia) 

else:
    print("a")
