'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''
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
    
