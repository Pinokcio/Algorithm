class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for i in range(len(cost)+1)]
        def getdp(n):
            if dp[n] != -1:
                return dp[n]
            dp[n] = min(getdp(n-1)+cost[n-1], getdp(n-2)+cost[n-2])
            return dp[n]
        dp[0] = 0
        dp[1] = 0
        return getdp(len(cost))
