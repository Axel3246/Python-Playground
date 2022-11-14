class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Si no está el ch regresamos la palabra
        if(ch not in word):
            return word
        else:
            R = word.find(ch) # encontramos la primera instancia de ch
            newWord = ""
            for i in range(R, 0, -1): # apendizamos el char a un nuevo string
                newWord += word[i]
            
            newWord += word[0] # apendizamos la primera letra
            newWord += word[R+1:len(word)] #apendizamos le resto
            return newWord     # regresamos la palabra