
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1
        suma = 0
        # Two Pointer Approach
        while(L < R):
            suma = numbers[L] + numbers[R] ## Check the sum of the idx
            if(suma == target): ## if equal return pointers + 1 (1-indexed array)
                return (L+1,R+1)
            elif (suma < target): ## we need a higher number, add L++
                L += 1
            else:
                R -= 1 # We need a lower number, subtract R--
        