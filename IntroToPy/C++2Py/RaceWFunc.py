

# Carrera
# Te estas preparando para una arrera de 10 kilometros y quieres saber en que tiempo debes de pasar por cada km para hacer un tiempo
# determinado.

# Indica los minutos en los que quieres terminar la carrera.
# Indica el tiempo en el cual debes de pasar por cada km para competar tu recorrido en el tiempo esperado.
from os import system

def totalMin(min):
    plus = 1
    print("Debes de hacer estos tiempos: ")
    for i in range(0, 10):
        K = (minutes/10)*plus
        print("K" + str(i+1) + ": " + str(float(K)))
        plus += 1

system("cls")
minutes = float(input("En cuantos minutos desead terminar tu carrera de 10 km: "))
totalMin(minutes)
