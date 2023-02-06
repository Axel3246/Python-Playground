#Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores (Ana y Juan).

ana = str(input())
juan = str(input())

analen = len(ana)
juanlen = len(juan)

#proceso piedra=a, papel=p, tijera=t

if (ana == 'a' or ana == 'p' or ana == 't') and (juan == 'a' or juan == 'p' or juan == 't'):
    if (ana == 'a'):
        if (juan == 'a'):
            print ("Empate")
        elif (juan == 'p'):
            print ("Gana Juan")
        else:
            print ("Gana Ana")
    elif (ana == 'p'):
        if (juan == 'p'):
            print ("Empate")
        elif (juan == 't'):
            print ("Gana Juan")
        else:
            print ("Gana Ana")
    elif (ana == 't'):
        if (juan == 't'):
            print ("Empate")
        elif (juan == 'a'):
            print ("Gana Juan")
        else:
            print ("Gana Ana")
else:
    if (analen>1 or juanlen>1):
        print ("Las tiradas deben ser un caracter")
    else:
        print ("Tirada incorrecta")
    


            


