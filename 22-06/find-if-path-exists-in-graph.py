from collections import deque, defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = deque()
        st = set()
        dic = defaultdict(list)
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
        q.append(source)
        st.add(source)
        while q:
            tmp = q.popleft()
            for n in dic[tmp]:
                if n not in st:
                    q.append(n)
                    st.add(n)
        if destination in st:
            return True
        return False
