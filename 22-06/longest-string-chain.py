import math
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = defaultdict(list)
        len_min = math.inf
        for w in words:
            dic[len(w)].append(w)
        ans = 0
        st = set()
        def dfs(ans, cur, n):
            #print(n, cur)
            st.add(cur)
            ans = max(ans, n)
            if n+1 in dic:
                for d in dic[n+1]:
                    if d in st:
                        continue
                    cnt = 0
                    for i in range(n+1):
                        if cnt == 0 and i == n:
                            cnt += 1
                            break
                        if cur[i - cnt] != d[i]:
                                cnt += 1
                        if cnt == 2:
                            break
                    if cnt == 1:
                        ans = max(ans, dfs(ans, d, n+1))
            return ans
        maxn = 0
        for i in sorted(dic):
            for d in dic[i]:
                if d in st:
                    continue
                len_min = i
                ans = max(ans, dfs(ans, d, i))
            maxn = max(maxn, ans - i + 1)
        return maxn
      
"""
dfs를 통해 해결함.
단어 길이에 따라 dictionary로 정리하여 길이가 작은 단어부터 확인하며 
길이가 1만큼 더 긴 단어과 비교했을 때 1만큼만 차이나면 dfs를 이어가고 아니면 멈춤
모든 단어에 대해 1번씩만 방문해야하므로 visit을 확인하는 set인 st를 만들어 방문을 확인함
"""
