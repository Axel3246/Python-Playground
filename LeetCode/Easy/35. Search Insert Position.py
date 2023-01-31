'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Values
        low = 0
        high = len(nums)-1
        
        # Binary Search
        while(low <= high):
            # Get mid
            mid = (low + high) // 2
            # If found, return idx
            if(nums[mid] == target):
                return mid
            # If mid value < target, update low to mid + 1, since its not in that part of arr
            elif(nums[mid] < target):
                low = mid + 1
            # Viceversa
            else:
                high = mid - 1
        # If not found, return low, since it'll be next possible index
        else:
            return low
