'''
You are given an array of strings names, and an array heights that 
consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
 
Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Helper array (tuple)
        res = []
        for i in range(0, len(names)):
            res.append(tuple([names[i],heights[i]]))
        # Append sorted descending names into new arr
        # ket = lambda x:x[1] gets the second element of the arr
        newres = [i[0] for i in sorted(res, key=lambda x:x[1], reverse=True)]
        # return names
        return newres