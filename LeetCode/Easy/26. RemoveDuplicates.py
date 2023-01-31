'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

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

            return k # Regresamos K
            
        