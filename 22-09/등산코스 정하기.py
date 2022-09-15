from collections import defaultdict
import heapq as hq
def solution(n, paths, gates, summits):
    path = {}
    for p in paths:
        if p[0] in path:
            path[p[0]][p[1]] = p[2]
        else:
            path[p[0]] = {p[1] : p[2]}
        if p[1] in path:
            path[p[1]][p[0]] = p[2]
        else:
            path[p[1]] = {p[0] : p[2]}
    heap = []
    visit = set()
    for g in gates:
        for p in path[g]:
            if (g, p) not in visit and (p, g) not in visit:
                hq.heappush(heap, (path[g][p], p))
                visit.add((g, p))
                visit.add((p, g))
    gates = set(gates)
    summits = set(summits)
    cur = 0
    intensity = 0
    result = []
    while heap:
        tmp = hq.heappop(heap)
        cur = tmp[1]
        intensity = max(intensity, tmp[0])
        if result != []:
            if result[1] < intensity:
                break
        if cur in summits:
            if result == []:
                result = [cur, intensity]
            elif result[0] > cur:
                result = [cur, intensity]
            continue
        for p in path[cur]:
            if (cur, p) not in visit and (p, cur) not in visit:
                hq.heappush(heap, (path[cur][p], p))
                visit.add((cur, p))
                visit.add((p, cur))
    return result
    
    
"""
gates에서 출발해서 summits까지 도착하는데 intensity가 가장 작은 루트를 고르는 문제
return : [summits, min_intensity]
gates에서 모든 경로를 탐색하되, summits에 도착하면 종료하거나, gates에는 닿지 않으며, intensity가 다른 루트보다 더 클 경우
방문하지 않는 경우를 구할 것
"""
