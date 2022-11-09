'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Si la lista tiene un size > 1 : hacemos algo
        if (len(nums) > 1):
            L = 0 # inicializamos en idx 0
            R = L+1 # inicializamos en L+1 (idx 1)
            
            # Iteramos la lista desde 0 hasta size -1
            for i in range(0, len(nums)-1, 1):
                if(nums[L] != 0): ## si nums[L] no contiene un 0, movemos L y R hacia la derecha
                    L += 1
                    R += 1
                else: # si nums[L] = 0
                    if(nums[R] != 0): # Checamos si en idx R hay un valor diff de 0
                        temp = nums[R] # Sí si, es un simple intercambio de valores
                        #print(nums[R])
                        nums[R] = nums[L]
                        nums[L] = temp
                        L += 1
                        R += 1
                    else: # si hay un 0 solo movemos R
                        R += 1 

                