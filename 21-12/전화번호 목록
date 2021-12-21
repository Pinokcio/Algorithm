import heapq
def solution(pb):
    heapq.heapify(pb)
    p = heapq.heappop(pb)
    while pb:
        print(pb)
        if p == pb[0][:len(p)]: 
            return False
        p = heapq.heappop(pb)
    return True
