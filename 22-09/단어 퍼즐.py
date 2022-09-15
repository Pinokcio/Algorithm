import math
import heapq as hq
        
def solution(strs, t):
    len_t = len(t)
    strs = set(strs)
    dp = [[0 for _ in range(5)] for _ in range(len_t)]
    for s in range(len_t):
        for i in range(1, 6):
            min_t = min(s+i, len_t)
            tmp = t[s:min_t]
            if tmp in strs:
                dp[s][i-1] = 1
            if min_t == len_t:
                break
    visit = set()
    heap = []
    for i in range(5):
        if dp[0][i] == 1:
            hq.heappush(heap, (dp[0][i], i+1))
    visit.add(0)
    while heap:
        tmp = hq.heappop(heap)
        cur = tmp[1]
        acu = tmp[0]
        if cur in visit:
            continue
        visit.add(cur)
        if cur == len_t:
            return acu
        for i in range(5):
            if dp[cur][i] == 1:
                hq.heappush(heap, (acu+1,(cur+i+1)))
    return -1
"""
모든 단어 조각의 길이는 1 이상 5 이하.
즉, banana를 예시로 들면
b/ba/ban/bana/banan이 strs에 있을 수도 있는 단어들이고,
a/an/ana/anan/anana가 다음으로 있을 수 있는 단어고,
n/na/nan/nana, a/an/ana, n/na, a와 같이 될 것이다.
만약 첫 경우에 ba, ban을 찾았다면[dp[1][2] = 1, dp[1][3] = 1] 
그 다음으로는 nana 혹은 ana가 있는지 찾으면 된다.[dp[3][6] = 1?, dp[2][6] = 1?]
이후에는 priorityqueue(heapq)를 사용했다.

만약 dp[1][3] = 1이면 dp[4][-1]까지를 찾아야할 것이다. 이 때 우선순위를 여기까지 방문하기 전에 사용한 단어의 갯수(cost)로
잡으면, visit.add(cur)로 두었을 때 cur까지는 해당 cost가 최소이기 때문에 다음에 똑같은 cur에 방문한 노드들을 무시할 수 있다.
이와 같은 방식으로 처음 스펠링부터 시작하여 최대 5개까지 단어를 살펴보며 해당 단어까지의 경로를 최적화(cost 최소화)하는 과정을 
반복하여 최종 스펠링까지 수행한다. 이 때 최종 스펠링에 도달한 순간의 cost가 최소이므로 (priorityqueue의 우선순위) 해당 값을 return한다.
만약 heap이 비었을 때까지 while을 반복하게 된다면 최종 스펠링에 도달할 수 없는 것이기 때문에 -1을 return한다.
"""
