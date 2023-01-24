class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lista = [] # lista para guardar
        maxSize = len(s) # max value
        minSize = 0  # 0
        # dependiendo cual apendizamos el valor
        for letter in s:
            if(letter == 'I'):
                lista.append(minSize)
                minSize += 1
            else:
                lista.append(maxSize)
                maxSize -= 1

        # checamos cual es el valor final y le damos append
        if(s[len(s) == 'I']):
            lista.append(minSize)
        else:
            lista.append(maxSize)
        
        # regresamos la lista
        return lista
