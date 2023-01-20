
# SOLUTION 1 -> USING SORTED ARRAYS
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # NOT OF SAME SIZES, RETURN FALSE
        if len(s) != len(t):
            return False
        # CREATE TWO ARRAYS, SORT THEM AND THEN COMPARE IF THE VALUES ARE EQUAL
        else:
            a = [i for i in s]
            b = [j for j in t]
            a.sort()
            b.sort()
            for i in range(0,len(b)):
                if b[i] != a[i]:
                    return False
            return True
        
        
# SOLUTION 2 -> USING SORTED() FUNCTION ON STRINGS
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # SORTED RETURNS STRING OR NUMBERS IN ORDER
        return sorted(s) == sorted(t)
    
# SOLUTION 3 -> COMMUNITY BEST: USING HASH TABLE / DICT WITH COUNTER
''' EXAMPLES
>>> from collections import Counter

>>> # Use a string as an argument
>>> Counter("mississippi")
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

>>> # Use a list as an argument
>>> Counter(list("mississippi"))
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


AT THE END JUST RETURN S == T
'''
