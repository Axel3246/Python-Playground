class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        # sublist[::-1] = [1,0,0] --> [0,0,1]
        lista = [sublist[::-1] for sublist in image]
        
        # intercambio de valores por 0, 1.
        for i in range(len(lista)): 
            for j in range(len(lista)):
                if (lista[i][j] == 0):
                    lista[i][j] = 1
                else:
                    lista[i][j] = 0

        return lista
        
            
        
'''
Mejor solución por la comunidad
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)): #recorre la matriz
            image[i] = image[i][::-1] # reversea la lista del iterador 0
            image[i] = [0 if x == 1 else 1 for x in image[i] ] # apendiza los valores correctos
        return image
'''