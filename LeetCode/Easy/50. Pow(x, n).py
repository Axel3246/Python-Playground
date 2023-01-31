'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # WE CAN TAKE ADVANTAGE OF PYTHON OPERATORS AND USE **
        return x**n