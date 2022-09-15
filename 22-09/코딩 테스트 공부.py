from collections import deque
import math

def solution(alp, cop, problems):
    req_alg = 0
    req_cod = 0
    max_alg = 0
    max_cod = 0
    for p in problems:
        req_alg = max(req_alg, p[0])
        req_cod = max(req_cod, p[1])
        max_alg = max(max_alg, p[2])
        max_cod = max(max_cod, p[3])
    if alp >= req_alg and cop >= req_cod:
        return 0
    
    dp = [[max(0, i-cop)+max(0, j-alp) for i in range(req_cod+1)] for j in range(req_alg+1)]
    
    for i in range(min(alp+1, req_alg+1)):
        for j in range(min(cop+1, req_cod+1)):
            dp[i][j] = 0

    for i in range(max(0, alp-max_alg-10), req_alg+1):
        for j in range(max(0, cop-max_cod-10), req_cod+1):
            for p in problems:
                if i >= p[0] and j >= p[1]:
                    min1 = req_alg if req_alg < i+p[2] else i+p[2]
                    min2 = req_cod if req_cod < j+p[3] else j+p[3]
                    dp[min1][min2] = dp[min1][min2] if dp[min1][min2] < dp[i][j] + p[4] else dp[i][j] + p[4]
    
    return dp[req_alg][req_cod]
            
    

"""
문제를 풀기 위해선 일정 이상의 알고력, 코딩력 필요
1. 1의 시간을 들여서 알고력 혹은 코딩력을 1 높일 수 있음
2. 각각은 문제를 풀어서 높일 수 있음
3. 문제 푸는데는 특정 시간이 필요하며 한 문제를 여러번 푸는 것도 가능
모든 문제를 풀기 위한 알고력과 코딩력을 얻는 최단시간을 구하는 문제
[알고요구, 코딩요구, 알고보상, 코딩보상, 들어가는 시간]

dp를 통해 시도해본다.
모든 문제를 풀기 위해 필요한 알고력, 코딩력을 구한다.
최대 시간복잡도 : 151 * 151 * 102 = 2,325,702
"""
