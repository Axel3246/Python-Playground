import random
import string
from words import words

def getValidWord(words):
    word = random.choice(words) # Get rand word
    
    # Mientras exista un dash o espacio
    while '-' in word or ' ' in word:
        word = random.choice(words) # Get rand word

    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letters of word
    #print(word)
    #print(wordLetters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters guessed
        
    while len(wordLetters) > 0:
        
        # Letter used
        # ' '.join(['a','b','c','x', 'cd']) -> 'a b c x cd
        print('You have used these letters: ', ' '.join(used_letters))
        
        # what current is word is (H - E L L O)
        # PD: WOW
        # Explicacion: Añade letra si esta en el set de used_letters, si no añade un dash
        # obedeciendo a la letra que encontramos
        wordList = [letra if letra in used_letters else '-' for letra in word]
        print("Current word: ", ' '.join(wordList))
        # Getting user input
        user_letter = input("Guess a letter: ").upper()
        # Caracter que no he usado
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # Eliminar la letra de la palabra por encontrar
            if user_letter in wordLetters:
                wordLetters.remove(user_letter)
        # Si ya se usó
        elif user_letter in used_letters:
            print (f"Already used the letter {user_letter}. Try again!")
        
        else:
            print("Invalid character. Try again!")
    else:
        print(f"Congrats! The word was {word}.")
        
    
hangman()