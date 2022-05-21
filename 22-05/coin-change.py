import math
minn = math.inf
class Solution:
    minn = math.inf
    def dfs(self, sumn, cnt, coins, amount, memo):
        if memo[sumn] <= cnt:
            return
        memo[sumn] = cnt
        if cnt >= self.minn:
            return 
        for c in coins:
            if sumn + c == amount:
                self.minn = min(self.minn, cnt+1)
                return 
            if sumn + c < amount:
                self.dfs(sumn + c, cnt + 1, coins, amount, memo)
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(10001)]
        coins.sort(reverse = True)
        self.dfs(0, 0, coins, amount, memo)
        if amount == 0:
            return 0
        if self.minn == math.inf:
            return -1
        return self.minn
        
# memoization과 dfs를 이용한 풀이
#################################################################
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(10001)]
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return dp[amount] if dp[amount] != math.inf else -1
# dp를 이용한 풀이
