#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if((nums[i] + nums[j]) == target):
                    return i,j
        
        
        
# @lc code=end

### HASHMAP SOLUTION (TOP)

nums = [3,2,4]
target = 6

# EMPTY HASHMAP
hashmap = {}
# TRAVERSING NUM ARRAY
for i in range(len(nums)):
    # GETTING THE RESIDUAL VALUE OF NUMS - TARGET. THIS WAY WE'LL BE ABLE TO FIND LATER IF THERE EXIST 
    # A NUM[I] THAT IS A COMPLIMENT OF ANOTHER NUMBER
    complement = target - nums[i]
    #print(f'Complement es {complement}')
    # WHEN WE FIND IT WE RETURN THE INDEXES
    if complement in hashmap:
        print ([i, hashmap[complement]])
    # ELSE WE INCLUDE NUMS[I] AND THE ITERATOR IN THE HASHMAP
    hashmap[nums[i]] = i
    #print(f'En {i} el hash tiene',hashmap)
    
#print(hashmap)
    
