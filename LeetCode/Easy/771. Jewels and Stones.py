'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lst1 = list(jewels)
        lst2 = list(stones)
        print(lst1, lst2)
        c = 0
        # Basically just count how many times the letter appears
        for stones in lst2:
            count = 0
            for jewel in lst1:
                if count == 0:
                    # Sum of words we can't use
                    if jewel in stones:
                        c += 1
                        count = 1
        # Return true number of words len - c
        return c
