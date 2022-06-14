import math
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        len_y = len(triangle)
        dp = [[math.inf for i in range(j+1)] for j in range(len_y)]
        dp[0][0] = triangle[0][0]
        def getdp(i, j):
            if i == 0:
                return dp[i][0]
            if dp[i][j] != math.inf:
                return dp[i][j]
            if j == 0:
                dp[i][j] = getdp(i-1, j)+triangle[i][j]
            elif j == i:
                dp[i][j] = getdp(i-1, j-1)+triangle[i][j]
            else:
                dp[i][j] = min(getdp(i-1, j-1), getdp(i-1, j)) + triangle[i][j]
            return dp[i][j]
        minn = []
        for i in range(len_y):
            minn.append(getdp(len_y-1,i))
        return min(minn)
