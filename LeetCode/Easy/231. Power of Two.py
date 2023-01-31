'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
'''

import math

class Solution:
    # Recursive
    def isPowerOfTwo(self, n: int) -> bool:
        # if power is 0 its false
        if n == 0:
            return False
        # if its 1 its true, since its the lowest number we can achive to divide by 2
        if n == 1:
            return True
        # if we find 1 as a residue of MOD its also false
        if n % 2 == 1:
            return False
        # we just return nexc value of the num divided by 2 and check for cases
        return self.isPowerOfTwo(n/2)