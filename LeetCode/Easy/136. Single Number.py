'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmap = {}
        # Traverse hashmap and count occurences
        for i in nums:
            hmap[i] = 1 + hmap.get(i,0)
        # Return min key - value matching
        return min(hmap, key = hmap.get)