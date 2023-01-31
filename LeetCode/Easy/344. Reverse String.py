'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0 # Left Pointer
        R = len(s)-1 # Rigtmost Pointer
        while(L < R): # Middle element wont be changed
            s[L], s[R] = s[R], s[L] # We exchange elements
            L += 1 # idx + 1
            R -= 1 # idx - 1
            #print(s) 
