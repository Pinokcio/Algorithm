def solution(lines):
    dp = [0 for _ in range(200)]
    for l in lines:
        for k in range(min(l)+99, max(l)+99):
            dp[k] += 1
    ret = 0
    for d in dp:
        if d>=2:
            ret += 1
    return ret
