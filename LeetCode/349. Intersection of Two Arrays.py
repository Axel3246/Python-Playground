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