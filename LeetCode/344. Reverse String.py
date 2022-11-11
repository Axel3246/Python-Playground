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
