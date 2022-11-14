class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        size = max(len(word1), len(word2)) # Get max size 
        L = 0 # P1
        L2 = 0 #P2
        newword = "" #New string
        while size: # while size > 0
            if(L < len(word1)): # Check for st1
                newword += word1[L]
                L += 1
            if(L2 < len(word2)): # Check for st2
                newword += word2[L2]
                L2 += 1
            size -= 1 # Decrease count
        # [n:] para el final de cualquier
        return newword #return word

        