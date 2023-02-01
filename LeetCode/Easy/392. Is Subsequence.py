'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Base cases
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        else:
            R = 0 # For T
            L = 0 # For S
            # We check every char of T while L != size of S
            while(R < len(t) and L < len(s)):
                # If we find a match we sum +1 to L and R counters
                if s[L] == t[R]:
                    L += 1
                    R += 1
                else:
                    # Else we continue our serch in T
                    R += 1
            # If L == size of s its true
            return L == len(s)