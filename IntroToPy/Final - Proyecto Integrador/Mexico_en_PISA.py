import time

def niveluno():
    Puntaje = 0
    time.sleep(1.5)
    print("Ahora es momento que resuelvas el primer problema en este primer nivel")
    time.sleep(1)
    print ("Me vas a dar el resultado de la operación: 54 + 46")
    while True:
        try:
            Problema1A= int(input("Dame tu respuesta: "))
        except:
            print ("Debe ser un valor numerico")
            continue
        if Problema1A==100:
            Puntaje = Puntaje + 2
            print ("Excelenete trabajo, has ganado: 2 puntos")
        else:
            print ("Carnal, te hace falta saber sumar, la respuesta correcta es 100, por favor, repasa las sumas.")
        break 
    
    time.sleep(1.3)
    print ("Ahora, es turno del problema 2")
    time.sleep(1)
    print ("Al igual que el anterior, esta tambien es una suma, pero un poco mas complicada. Vas a darme el resultado de: 14566 + 3452")
    while True:
        try:
            problema2a= int(input("Dame tu respuesta: "))
        except:
            print ("Debe ser un valor numerico")
            continue
        if problema2a==18018:
            Puntaje = Puntaje + 2
            print ("Muy buen trabajo, has ganado: 2 puntos")
        else:
            print ("Aunque sean numeros grandes, son sumas amiguito. La respuesta correcta era 18018, debes de repasarlas más")
        break

#Problema 3
    time.sleep(1.3)
    print ("En este tercer problema, entramos ahora con las restas")
    time.sleep(1)
    print ("Dame el resultado de la resta: 34-56")
    while True:
        try:
            problema3a= int(input("Dame tu respuesta: "))
        except:
            print ("Debe ser un valor numerico")
            continue
        if problema3a==-22:
            Puntaje = Puntaje + 2
            print ("Muy buen trabajo, has ganado: 2 puntos")
        else:
            print ("¿Qué pasó aquí?, ¿Ya comenzamos a batallar?, hay que repasar las restas, la resuesta correcta era -22 recuerda que cuando restas un numero que es mayor que otro, el resultado es negativo")
        break

#Problema 4
    time.sleep(1.3)
    print ("Este es el  problema 4 del nivel, una última resta")
    time.sleep(1)
    print ("Vas a darme el resultado de la resta: 7458-5217")
    while True:
        try:
            problema4a= int(input("Dame tu respuesta: "))
        except:
            print ("Debe ser un valor numerico")
            continue
        if problema4a==2241:
            Puntaje = Puntaje + 2
            print ("Excelente trabajo, has ganado: 2 puntos")
        else:
            print ("Que esté mas larga no es excusa para no saber restar, la respuesta correcta era 2241, sigue repasando restas amiguito")
        break   

#Problema 5
    time.sleep(1.3)
    print ("Aquí tendrás que resolver una combinación de todas las operaciones vistas hasta el momento")
    time.sleep(1)
    print ("Vas a darme el resultado de: 2345-3456+7890-1+45")
    while True:
        try:
            problema5a= int(input("Dame tu respuesta: "))
        except:
            print ("Debe ser un valor numerico")
            continue
        if problema5a==6823:
            Puntaje = Puntaje + 2
            print ("Excelente trabajo, has ganado: 2 puntos")
        else:
            print ("Lo lamento, tu respuesta es incorrecta, la respuesta correcta era 6823, necesitas regresar a repasar mucho las sumas y las restas")
        break
    
    time.sleep(1.5)
    print("Al terminar este nivel, reflexiona sobre el total de puntos que obtuviste, piensa donde te equivocaste, y repasa lo que no sabes. Tu puntaje fue: "+ str(Puntaje))

    
def niveldos():    
    time.sleep(1.5)
    Puntaje = 0
    print("Bienvenido al segundo nivel: Multiplicación y División\nMenciona el resultado de la siguiente operación: 12 x 12 ")
    while True:
        try:
            Problema2A= int(input('Tu respuesta: '))
        except:
            print('Escribe una respuesta numérica')
            continue
        if Problema2A == 144:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Repasa las multiplicaciones. El resultado es 144.")
        break
    
    time.sleep(1.3)
    print("¿Cuál es el resultado de 120 x 5?")
    while True:
        try:
            Problema2B = int(input('Tu respuesta: '))
        except:
            print('Escribe una respuesta numérica')
            continue
        if Problema2B == 600:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Siempre puedes volver a intentar. El resultado es 600.")
        break
    
    time.sleep(1.3)
    print("Ya casi acabamos. Ahora tocan divisiones: ¿Cuál es el resultado de 81 / 3?")
    while True:
        try:
            Problema2C= int(input('Tu respuesta: '))
        except:
            print("Escribe una respuesta numérica")
            continue
        if Problema2C == 27:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Repasa la división. El resultado es 27.")
        break

    time.sleep(1.3)
    print("¿Cuál es el resultado de 25 / 2?")
    while True:
        try:
            Problema2D= float(input('Tu respuesta: '))
        except:
            print("Escribe una respuesta numérica")
            continue
        if Problema2D == 12.5:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("El resultado es 12.5.")
        break
    
    time.sleep(1.3)
    print("El útlimo: ¿Cuál es el resultado de 2500 x 4?")
    while True:
        try:
            Problema2E= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema2E == 10000:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Aun te falta practicar. El resultado es 10000.")
        break
    
    time.sleep(1.3)
    if Puntaje == 2 or Puntaje == 0:
        print("Práctica más este tema. Siempre se puede mejorar. Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 4:
        print("Te falta practicar un poco más. ¡Si se puede! Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 6:
        print("Ya vas comprendiedo el tema. ¿Otra oportunidad? Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 8:
        print("¡Nada Mal! Obtuviste " + str(Puntaje) + " puntos")
    else:
        print("Excelente. ¡Sigue así! Obtuviste " + str(Puntaje) + " puntos")

def niveltres():

    time.sleep(1.5)
    Puntaje = 0
    #problema1
    print("Bienvenido al tercer nivel: Exponentes\nMenciona el resultado de la siguiente operación: 5^3 ")
    while True:
        try:
            Problema3A= int(input('Respuesta: '))
        except:
            print('Inserta sólo valores numéricos')
            continue
        if Problema3A == 125:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Cuidado con el procedimiento. El resultado es 125")
        break
    
    time.sleep(1.3)
    print("¿Cuál es el resultado de 20^4?")
    while True:
        try:
            Problema3B= int(input('Respuesta: '))
        except:
            print('Inserta sólo valores numéricos')
            continue
        if Problema3B == 160000:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("El resultado es 160000")
        break
    
    time.sleep(1.3)
    #problema3
    print("Ya casi acabamos. Exponentes fraccionarios: ¿Cuál es el resultado de 16^(1/2)?")
    while True:
        try:
            Problema3C= int(input('Respuesta: '))
        except:
            print('Inserta sólo valores numéricos')
            continue
        if Problema3C == 4:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Incorrecto, el resultado es 4")
        break
    
    time.sleep(1.3)
    print("¿Cuál es el resultado de 1^64?")
    while True:
        try:
            Problema3D= int(input('Respuesta: '))
        except:
            print('Inserta sólo valores numéricos')
            continue
        if Problema3D == 1:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Incorrecto, el resultado es 1")
        break

    print("Finalmente: ¿Cuál es el resultado de 0^4?")
    while True:
        try:
            Problema3F= int(input('Respuesta: '))
        except:
            print('Inserta sólo valores numéricos')
            continue
        if Problema3F == 0:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("No se te olvide que cualquier numero al que se eleve 0, es 0")
        break

    time.sleep(1.3)
    #resultados
    print("Vamos a ver tu puntaje")
    time.sleep(1.3)
    if Puntaje == 2 or Puntaje == 0:
        print("Práctica más este tema. Siempre se puede mejorar. Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 4:
        print("Te falta practicar un poco más. ¡Si se puede! Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 6:
        print("Ya vas comprendiedo el tema. ¿Otra oportunidad? Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 8:
        print("¡Nada Mal! Obtuviste " + str(Puntaje) + " puntos")
    else:
        print("Excelente. ¡Sigue así! Obtuviste " + str(Puntaje) + " puntos")


def nivelcuatro():
    Puntaje=0
    time.sleep(1.5)
    print("Bienvenido al cuarto nivel: Álgebra, ¿Estás listo?\nMenciona el valor de a en la siguiente operación: 17 + a = 30 ")
    while True:
        try:
            Problema4A= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema4A == 13:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Ojo ahí, el 17 pasa restando. La respuesta es 13")
        break

    time.sleep(1.3)
    print("¿Cuál es el valor a en la siguiente ecuación: 2a = 10? ")
    while True:
        try:
            Problema4B= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema4B == 5:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Cuidado con el procedimiento. Recuerda que el  2 pasa dividiendo. La respuesta es 5")
        break

    time.sleep(1.3)
    print("¿Qué valor tiene la a en la siguiente ecuación: 12 + 7a = 40?")
    while True:
        try:
            Problema4C= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema4C == 4:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Ten cuidado con estas, el 12 pasa restando al 40 y el 7 dividiendo a todo. La respuesta es 4.")
        break

     
    time.sleep(1.3)
    print("Estás cerca de terminar. ¿Qué valor tiene a en la siguiente ecuación: 2a + a + 5 - 1 = 10 + 2 - a")
    while True:
        try:
            Problema4D= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema4D == 2:
            Puntaje = Puntaje + 2
            print ("¡Bien!, llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Ten cuidado, no estaba tan complicada")
        break
     
    time.sleep(1.3)
    print("Ya casi terminamos. ¿Qué valor tiene b en la siguiente ecuación cuando a = 2: ab + a(ab) = 30?")
    while True:
        try:
            Problema4E= int(input('Tu respuesta: '))
        except:
            print("Escribe un valor numérico")
            continue
        if Problema4E == 5:
            Puntaje = Puntaje + 2
            print ("Excelente, era una dificil! Llevas " + str(Puntaje) + " punto(s)")
        else:
            print("Buen intento, pero esa no es la respuesta. Debes de seguir practicando")
        break
     
    print("¡Terminaste! Vamos a ver tu puntaje")
    time.sleep(1.3)
    if Puntaje == 2 or Puntaje == 0:
        print("Práctica más este tema. Siempre se puede mejorar. Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 4:
        print("Te falta practicar un poco más. ¡Si se puede! Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 6:
        print("Ya vas comprendiedo el tema. ¿Otra oportunidad? Obtuviste " + str(Puntaje) + " puntos")
    elif Puntaje == 8:
        print("¡Nada Mal! Obtuviste " + str(Puntaje) + " puntos")
    else:
        print("Excelente. ¡Sigue así! Obtuviste " + str(Puntaje) + " puntos")


def seleccionDos():
    print('Inserta un nivel adecuado')
    nivel = str(input(" Nivel: "))
    if nivel == "1":
        print("Seleccionaste el nivel 1")
        niveluno()
    elif nivel == "2":
        print("Seleccionaste el nivel 2")
        niveldos()
    elif nivel == "3":
        print("Seleccionaste el nivel 3")
        niveltres()
    elif nivel =="4":
        print("Seleccionaste el nivel 4")
        nivelcuatro()
    else:
        seleccionDos()

def seleccion():
    print("¿Qué nivel deseas reforzar? \n 1.Suma y Resta \n 2.Multiplicación y División \n 3.Exponentes \n 4.Algebra")
    nivel = str(input(" Nivel: "))
    if nivel == "1":
        print("Seleccionaste el nivel 1")
        niveluno()
    elif nivel == "2":
        print("Seleccionaste el nivel 2")
        niveldos()
    elif nivel == "3":
        print("Seleccionaste el nivel 3")
        niveltres()
    elif nivel =="4":
        print("Seleccionaste el nivel 4")
        nivelcuatro()
    else:
        seleccionDos()

seleccion()