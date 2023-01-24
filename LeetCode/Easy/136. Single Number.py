class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmap = {}
        # Traverse hashmap and count occurences
        for i in nums:
            hmap[i] = 1 + hmap.get(i,0)
        # Return min key - value matching
        return min(hmap, key = hmap.get)
    
'''
OTHER SOLUTIONS USING ^
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 #n ^ 0 = n 
        
        for n in nums:
            
            res = n ^ res 
            print(n,res)
        
        return res
        
        it does the XOR operation on the bit representation of the number;

8 => 1000
15 =>1111
8 ^ 15 = 7 => 0111
7 ^ 8 = 15 => 1111
'''