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
