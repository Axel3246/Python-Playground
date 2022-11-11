class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ") # Separamos el string a partir de los espacios
        lista = [word[::-1] for word in split] # Volteamos la palabra por cada palabra en el split
        
        '''
        for word in split:
            lista.append(word[::-1])
        '''
        
        return ' '.join(lista) # los regresamos con los espacios deseados usando join