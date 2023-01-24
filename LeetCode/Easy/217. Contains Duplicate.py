class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # SORT THE ARRAY
        nums.sort()
        # LOOP THROUGH I AND I+1. THIS WILL GET US THE DUPLICATE IN THE BEST CASE. 
        for i in range(0, len(nums)-1, 1):
            if (nums[i] == nums[i+1]):
                return True
        return False