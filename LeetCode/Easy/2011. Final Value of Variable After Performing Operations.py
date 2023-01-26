'''
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
'''

# Basically check for ++ or --
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        c = 0
        for i in operations:
            if "++" in i:
                c += 1
            elif "--" in i:
                c -= 1
        return c