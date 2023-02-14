'''
You are given an m x n integer grid accounts where accounts[i][j] 
is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

'''

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Max Value
        top = 0
        # Traverse arr of arr
        for i in accounts:
            # Sum
            suma = 0
            # J iter for arr
            for j in i:
                suma += j
            # Compute max
            top = max(top, suma)
        # Return top
        return top