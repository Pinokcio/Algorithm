class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_x = len(grid[0])
        len_y = len(grid)
        dp = [[0 for _ in range(len_x)] for _ in range(len_y)]
        dp[0] = grid[0]
        
        for i in range(len_y):
            for j in range(len_x):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[len_y-1][len_x-1]
