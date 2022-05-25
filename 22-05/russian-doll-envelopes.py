from collections import defaultdict
import math
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dic = defaultdict(list)
        envelopes.sort(key = lambda x : [x[0], -x[1]])
        for e in envelopes:
            dic[e[0]].append(e[1])
        #최대한 뒷쪽에 최대한 작은수로
        res = []
        len_r = 0
        #print(dic)
        for d in dic:
            for idx, l in enumerate(dic[d]):
                if (len_r == 0 or res[-1] < l):
                    res.append(l)
                    len_r += 1
                else:
                    s = 0
                    e = len_r-1
                    while s<=e:
                        mid = (s+e)//2
                        if res[mid] < l:
                            s = mid + 1
                        else:
                            e = mid - 1
                    res[s] = l
            #print(res)
        return len(res)
