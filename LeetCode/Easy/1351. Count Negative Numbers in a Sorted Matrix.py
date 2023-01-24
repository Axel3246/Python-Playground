class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        # Just traverse the matrix and count occurences
        for i in grid:
            for j in i:
                if j < 0:
                    c += 1

        return c