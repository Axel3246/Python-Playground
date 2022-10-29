import random

# Función para que la computadora adivine un numero
# Complejidad: Best O(1), Worst O(max)
def guessing(max):

    # Min
    low = 1
    # Num x adivinar
    num = max
    # Hint
    retro = '';
    while retro != 'C':
        # Si no coincide se saca un randInt en el rango
        if low != num:
            cpuGuess = random.randint(low, num)
        # Directamente diremos que lo encontró
        else:
            cpuGuess = low
        # Hint Input
        retro = input(f"Is {cpuGuess} the number? (L / H / C): ")
        if retro == 'H':
            num = cpuGuess - 1
        elif retro == 'L':
            low = cpuGuess + 1
        else:
            print(f"Yeah! The number was {num}!")
            
num = 100
guessing(num)
