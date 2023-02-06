# Funcion que calcula el siguiente dia de meses con 31 dias
def treintauno(dia, mes, año):

    if dia > 0 and dia < 31:
        dia = dia + 1
    else:
        mes = mes + 1
        dia = 1

    imprimir(dia, mes, año)
    
# Funcion que calcula el siguiente dia de meses con 30 dias
def treinta(dia, mes, año):

  if dia > 0 and dia < 30:
      dia = dia + 1
  else:
      mes = mes + 1
      dia = 1

  imprimir(dia, mes, año)

def bisiesto(dia, mes, año):
    if dia > 0 and dia < 29:
        dia = dia + 1
    elif dia == 29:
        mes = mes + 1
        dia = 1

    imprimir(dia, mes, año)
    
def nobisiesto(dia, mes, año):
    if dia > 0 and dia < 28:
        dia = dia + 1
        imprimir(dia, mes, año)
    elif dia == 28:
        mes = mes + 1
        dia = 1  
        imprimir(dia, mes, año)
    else:
        print("Datos Invalidos")


def diciembre(dia, mes, año):
    if dia > 0 and dia < 31:
        dia = dia + 1
    else:
        año = año + 1
        mes = 1
        dia = 1

    imprimir(dia, mes, año)

# Imprimir
def imprimir(d, m ,a):
    
    print('Año:', a)
    print('Mes:', m)
    print('Día:', d)


año = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Dia: "))

        
if ((mes <= 12 and mes >= 1) and (año >=0) and (dia > 0 and dia < 32)):

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:

        treintauno(dia, mes, año)

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
      
        treinta(dia,mes,año)
    
    elif mes == 2:

        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            
            bisiesto(dia, mes, año)
            
        else:
            
            nobisiesto(dia,mes,año)
    
    elif mes == 12:

        diciembre(dia, mes, año)


else:
    print("Datos Invalidos")
    

