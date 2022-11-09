class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #print(len(nums))
        
        if (len(nums) == 1): # Si es un elemento, retornamos size
            return 1
        elif (len(nums) == 2): # Si son dos retornamos los elementos únicos
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        else:
            k = 1 # size
            L = 0 # izq
            R = 1 # izq + 1
            
            for R in range(1, len(nums)): # iterar el array
                if(nums[R] == nums[L]): # si son iguales aumentamos R
                    R += 1
                elif (nums[R] != nums[L]): # si no son iguales cambiamos al adyacente de L por R y sumamos 1 al size y a L. R se iterará arriba si aun puede
                    temp = nums[R]
                    nums[R] = nums[L+1]
                    nums[L+1] = temp
                    L += 1
                    k += 1
                
               
            #rint(k)
            return k # Regresamos K
            
        