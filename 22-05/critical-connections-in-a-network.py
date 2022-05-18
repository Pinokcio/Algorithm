from collections import deque
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for a,b in connections:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        disc, low, time, ans = [0] * n, [0] * n, [1], []
        def dfs(curr: int, prev: int):
            disc[curr] = low[curr] = time[0]
            print(low)
            time[0] += 1
            for next in edgeMap[curr]:
                if not disc[next]: #disc가 0이면 해당 노드는 아직 방문하지 않은 것
                    dfs(next, curr) 
                    low[curr] = min(low[curr], low[next])
                elif next != prev: #방문했었지만 현재 노드가 출발했던 곳이 아닌 노드, back edge
                    low[curr] = min(low[curr], disc[next])
                if low[next] > disc[curr]: #현재 노드의 노드가 갈 수 있는 곳 중 가장 작은 값이 현재 노드보다 time이 크다 ==> 자식 노드가 현재 노드와 연결돼있지 않으며 더 나중에 방문되었다. == 사이클이 존재하지 않는다.
                    ans.append([curr, next])
        dfs(0, -1)
        return ans
#tarjan's algorithm이라고 한다.
#strongly connected component(scc)를 찾는 알고리즘이다.
#disc, low, time이 있는데, 이는 각각 
    #discoverd time, 몇번째로 방문한 노드인지, 
    #현재 노드를 루트로 하는 서브트리 중 간선 하나로 갈 수 있는 노드 중 가장 작은 노드, 
    #현재 몇번째 dfs인지를 나타낸다.
#time이 1 늘 때마다 dfs의 depth가 1씩 증가하는 것이며
