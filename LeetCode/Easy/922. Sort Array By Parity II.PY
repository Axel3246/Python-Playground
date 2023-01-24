class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #nums.sort()
        #res = []
        #searching for odd
        flag = True
        L = 0
        R = len(nums)-1
        while(L != R):
            # searching for odd
            if flag:
                if nums[L] % 2 == 0:
                    L += 1
                    flag = False
                elif nums[L] % 2 != 0:
                    if nums[R] % 2 == 0:
                        nums[L], nums[R] = nums[R], nums[L]
                        L += 1
                        R = len(nums)-1
                        flag = False
                    else:
                        R -= 1
            else:
                if nums[L] % 2 == 1:
                    L += 1
                    flag = True
                    continue
                elif nums[L] % 2 != 1:
                    if nums[R] % 2 == 1:
                        nums[L], nums[R] = nums[R], nums[L]
                        L += 1
                        R = len(nums)-1
                        flag = True
                    else:
                        R -= 1
        
        return nums
                

'''

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        e = 0
        o = 1
        for i in nums:
            if i%2==0:
                res[e] = i
                e+=2
            else:
                res[o] = i
                o+=2
        return res
    
            
            
'''