from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_x, len_y = len(matrix[0]), len(matrix)
        visit = [[-1 for  _ in range(len_x)] for _ in range(len_y)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        q = deque()
        q.append([0, 0, 0])
        visit[0][0] = 0
        while q:
            cur = q.popleft()
            if cur[2] < visit[cur[1]][cur[0]]:
                continue
            for k in range(4):
                nx = cur[0] + dx[k]
                ny = cur[1] + dy[k]
                if 0<=nx<len_x and 0<=ny<len_y:
                    if matrix[ny][nx] > matrix[cur[1]][cur[0]]:
                        if visit[ny][nx] < cur[2] + 1:
                            visit[ny][nx] = cur[2] + 1
                            q.append([nx, ny, cur[2] + 1])
                    elif visit[ny][nx] == -1:
                        visit[ny][nx] = 0
                        q.append([nx, ny, 0])
        return max([max(i) for i in visit]) + 1
