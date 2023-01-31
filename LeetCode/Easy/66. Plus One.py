'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # MAP AND JOIN ALL INTEGERS TO STRING
        a = int(''.join(map(str,digits)))
        # SUM ONE
        a += 1
        # USE EVAL TO CREATE NEW LIST WITH THE CHARACTERS AS INT
        b = [eval(num) for num in str(a)]
        return b

'''
similar solution, but i guess its less time consuming because it doesn't use list comprehension to eval every char

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number += 1
        return map(int,str(number))
'''