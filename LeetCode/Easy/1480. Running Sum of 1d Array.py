'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

'''
# Just keep last sum and sum to curr num
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lo = 0
        res = []
        for num in nums:
            res.append(num + lo)
            lo += num
        return res