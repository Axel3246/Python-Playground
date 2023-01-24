class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = {}
        # Check possible appearence (needs to be revisited for condition n / 2)
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        #print(hashmap)
        # return max key - value 
        return max(hashmap, key = hashmap.get)