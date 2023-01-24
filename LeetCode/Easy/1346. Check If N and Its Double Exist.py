class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        d = set() # set de los numeros
        for numero in arr:
            if numero * 2 in d or numero * 0.5 in d: # el doble de numero o la mitad del numero en el set
                return True
            d.add(numero)
        return False    
    
    ''' 
       for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i]*2 == arr[j] or arr[j]*2 == arr[i]:
                    return True
        return False
        '''