'''
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Map ta arr to a str of nums
        nmstr = "".join(map(str,num))
        # Create a new variable to store the sum 
        nmint = int(nmstr) + k
        # Use list comprehesion to return the num
        return [int(i) for i in str(nmint)]
        