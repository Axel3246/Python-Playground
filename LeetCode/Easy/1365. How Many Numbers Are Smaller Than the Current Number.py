'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(0,len(nums)-1):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i] and nums[j] != nums[i]:
                    res[i] += 1
                elif nums[j] > nums[i]:
                    res[j] += 1

        return res
    
    
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        currentNo=None
        smallerNo=0
        counter={}
        for num in sortedNums:
            if num!=currentNo:
                counter[num]=smallerNo
                currentNo=num
            smallerNo+=1
        return [counter[x] for x in nums]
                        
'''