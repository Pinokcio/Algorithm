from collections import deque, defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = max(dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1] else dp[i][j-1], dp[i-1][j])
        return len1 + len2 - dp[-1][-1]*2
"""
word1과 word2를 하나씩 비교하면서 같은 spell에 대해 서로 어떤 인덱스와 매칭시켜야 가장 길게 매칭시킬 수 있는지를 계산하는 문제이다. 
dp[i][0] and dp[0][j]는 전부 0으로 초기화
dp[i][j] : word1의 i-1번째와 word2의 j-1번째를 비교할 때 이전을 포함하여 일치하는 최대 string 길이
dp[i][j] = max(dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1] else dp[i][j-1], dp[i-1][j])
"""
