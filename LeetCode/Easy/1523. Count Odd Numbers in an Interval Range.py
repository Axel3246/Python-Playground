'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
'''

class Solution:

    def notOdd(self, num):
        return True if num % 2 == 0 else False

    def countOdds(self, low: int, high: int) -> int:
        # Check for low first odd (lo + 1)
        if self.notOdd(low):
            low += 1
        # Check for high first odd (hi - 1)
        if self.notOdd(high):
            high -= 1

        # Return formula (last odd (hi) - first odd (lo)) / 2 (two nums) + 1 (inclusive)
        return int((high-low)/2 + 1)

'''
-- Procedure --
 1. Pick the first odd integer.
 2. Pick the last odd integer.
 3. Find the difference.
 4. Divide by the interval (in this case 2, since the positive difference between  any two odd integers is 2).
 5. Add 1 for an inclusive range.
 '''