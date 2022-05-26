from collections import deque, defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1 for _ in range(len(rains))]
        arr = [] #중복 index
        dry = [] #dry index
        len_d = 0
        lake = defaultdict(int)
        for e, r in enumerate(rains):
            if r == 0:
                dry.append(e)
                len_d += 1
            else:
                if lake[r] == 0:
                    lake[r] = e+1
                else: #lake[r]보다 크거나 같은 가장 작은 index                   
                    start = 0
                    end = len_d-1
                    while start<=end:
                        mid = (start+end)//2
                        if dry[mid] < lake[r]:
                            start = mid + 1
                        else:
                            end = mid - 1
                    if len_d == 0 or start >= len_d:
                        return []
                    if dry[start] >= lake[r]:
                        res[dry[start]] = r
                        del dry[start]
                        len_d -= 1
                        lake[r] = e
                    else:
                        return []
                res[e] = -1
        return res
