class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(len(nums))
        if (len(nums) == 1):
            return 1
        elif (len(nums) == 2):
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        else:
            k = 1
            L = 0
            R = 1
            maxi = nums[L]
            for R in range(1, len(nums)):
                if(nums[R] == nums[L]):
                    R += 1
                elif (nums[R] != nums[L]):
                    temp = nums[R]
                    nums[R] = nums[L+1]
                    nums[L+1] = temp
                    L += 1
                    k += 1
                
               
            print(k)
            return k
            
        