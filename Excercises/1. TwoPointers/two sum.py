

#nums = [3, 2, 4]

nums = [2,7,11,15]
target = 9
# print(rightP)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if((nums[i] + nums[j]) == target):
            print (i,j)
            break


