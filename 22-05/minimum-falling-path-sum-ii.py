import math
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        len_y = len(grid)
        len_x = len(grid[0])
        dp = [[[0,i] for i in range(len_x)] for _ in range(len_y)]
        
        for i in range(len_x):
            dp[0][i][0] = grid[0][i]
        dp[0].sort()
        for i in range(1, len_y):
            for j in range(len_x):
                tmp = 0
                if dp[i-1][0][1] == j:
                    tmp = dp[i-1][1][0]
                else:
                    tmp = dp[i-1][0][0]
                dp[i][j][0] = tmp + grid[i][j]
            dp[i].sort()
        return dp[-1][0][0]
                            
