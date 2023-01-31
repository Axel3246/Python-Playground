'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create empty set
        mySet = set()
        # Create helper arr
        res = []
        # Fill set with arr1
        for i in nums1:
            mySet.add(i)
        # Check if there´s a match between arr1 & 2 and not in helper arr
        for j in nums2:
            if j in mySet:
                if j not in res:
                    res.append(j)

        return res

'''
BETTER

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return list(set_nums1 & set_nums2)
'''