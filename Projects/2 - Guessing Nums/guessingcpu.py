import random

# Función para imprimir un string
# Complejidad: O(1)
def printGuess():
    print("Guess a number between 1 and 10: ")
  
# Función para adivinar un numero utilizando concatenación e input normal
# Complejidad: O(n)  
def guessingCPU(randNum, num):
    while (num != randNum):
        if num < randNum:
            print("Sorry, guess again. Too low.")
            printGuess()
            num = int(input())
        elif num > randNum:
            print("Sorry, guess again. Too high.")
            printGuess()
            num = int(input())
    else:
        print("Nice! The number was " + str(randNum) + ".")
        
          
# Función para adivinar un numero utilizando f-strings
# Complejidad: Best O(1), Worst O(n)
def guessing(max):

    randNum = random.randint(1, max)
    num = 0
    while num != randNum:
        num = int(input(f"Guess a number between 1 and {max}: "))
        if num < randNum:
            print("Sorry, guess again. Too low.")
        if num > randNum:
            print("Sorry, guess again. Too high.")
    else:
        print(f"Nice! The number was {randNum}!")
            
            
#guessingCPU(randNum = random.randint(1,10), num = int(input()))
maxim = int(input(f"Till' what number would you like to guess? "))
guessing(maxim)
    
