'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check for every row
        # 2. Check for every column
        # 3. Check for every subsquare
        rows = defaultdict(set) # Track the rows
        colum = defaultdict(set) # Track the columns
        sqrs = defaultdict(set) # Track the sub squares. Key = [r // 3, c // 3] (subsquare)

        # Traverse Grid
        for r in range(9):
            for c in range(9):
                # Empty
                if board[r][c] == ".":
                    continue
                # Current Row, Column and Square check
                if (board[r][c] in rows[r] or 
                    board[r][c] in colum[c] or
                    board[r][c] in sqrs[(r // 3, c // 3)]):
                    return False
                # Adding to hashset
                colum[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[(r // 3, c // 3)].add(board[r][c])
        #print(colum,rows,sqrs,end="\n")
        return True
                