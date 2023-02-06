
año = int(input('¿Cuál es el año? '))
mes = int(input('¿Cuál es el mes? '))
dia = int(input('¿Cuál es el día? '))

if ((mes <= 12 and mes >= 1) and (año >= 0)):
    if (dia>0 and dia <30):
        if mes == 2:
            if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                if dia > 0 and dia < 29:
                    dia = dia + 1
                else:
                    mes = mes + 1
                    dia = 1
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
            if dia > 0 and dia < 31:
                dia = dia + 1
            elif dia == 31:
                mes = mes + 1
                dia = 1

        elif mes == 2:
            if dia > 0 and dia < 28:
                dia = dia + 1
            else:
                mes = mes + 1
                dia = 1
        # ----------------------------------------
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 0 and dia < 30:
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
    
else:
    print ("Esa fecha no existe")




