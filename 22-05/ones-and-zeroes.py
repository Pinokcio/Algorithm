import math
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[i.count("0"), i.count("1")] for i in strs]
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for a in arr:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i-a[0]>=0 and j-a[1]>=0:
                        dp[i][j] = max(dp[i][j], dp[i-a[0]][j-a[1]] + 1)
        return dp[m][n]
"""
조건을 만족하는 dp[i][j]에 arr을 하나씩 넣어보며 최솟값을 찾음
이 때, [i][j]를 m,n부터가 아닌 0,0부터 서치할 경우 업데이트 해주는 과정에서(11번째줄) 인덱스가 작은 배열로부터 값을 불러오므로
arr이 중복되어 계산될 수 있으므로 큰 인덱스에서부터 내림차순으로 서치하며 업데이트해준다.
"""
