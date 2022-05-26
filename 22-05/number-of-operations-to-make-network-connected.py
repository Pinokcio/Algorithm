class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def getParent(n):
            if parent[n] == n:
                return n
            parent[n] = getParent(parent[n])
            return parent[n]
        
        def union(a, b):
            if a > b:
                parent[a] = b
            else:
                parent[b] = a
                
        parent = [i for i in range(n)]
        cnt = 0
        tie = 1
        connections.sort(key = lambda x : [x[0], x[1]])
        for c in connections:
            p1 = getParent(c[0])
            p2 = getParent(c[1])
            if p1 != p2:
                union(p1, p2)
                tie += 1
            else:
                cnt += 1
        if n - tie <= cnt:
            return n-tie
        else:
            return -1
