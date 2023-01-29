'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
'''

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Create Sets for Row and Column
        row = defaultdict(set)
        col = defaultdict(set)
        #print(len(matrix))
        # Traverse Matrix Lenght
        for r in range(0, len(matrix)):
            for c in range(0,len(matrix)):
                # If we find a dupe, it means the num chain has been broken. Return false
                if (matrix[r][c] in row[r] or 
                    matrix[r][c] in col[c]):
                    return False
                # Add to set
                col[c].add(matrix[r][c])
                row[r].add(matrix[r][c])
        # We don't find dupes. 
        return True