from collections import deque
def solution(n, edge):
    length = len(edge)
    memo = [0]*(n+1)
    me = [[]for i in range(0,n+1)]
    for i in edge:
        me[i[0]].append(i[1])
        me[i[1]].append(i[0])
    for i in range(0, n+1):
        memo[i] = 0
    q = deque()
    q.append(1)
    m = [0]*(n+1)
    while q:
        cur = q.popleft()
        m[cur] = 1
        for i in me[cur]:
            if m[i] != 1 and i not in q:
                memo[i] = memo[cur] + 1
                q.append(i)
    maxn = 0
    cnt = 0 
    for i in range(2, n+1):
        if maxn < memo[i]:
            maxn = memo[i]
            cnt = 1 
        elif maxn == memo[i]:
            cnt += 1
    return cnt
    
    """처음엔 deque가 아닌 list로 queue를 대신하여 사용함. 이때 while문과 그 내부 사용에 있어 O(N)이라는 시간복잡도로 인해 timeout 발생. deque를 사용하여 O(1)로 줄임으로써 해결"""
