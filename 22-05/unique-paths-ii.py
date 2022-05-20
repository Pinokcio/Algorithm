from collections import deque
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dx = [1, 0]
        dy = [0, 1]
        len_x = len(obstacleGrid[0])
        len_y = len(obstacleGrid)
        visit = [[0 for _ in range(len_x)] for _ in range(len_y)]
        if obstacleGrid[0][0] == 0:
            visit[0][0] = 1
        for i in range(len_y):
            for j in range(len_x):
                if obstacleGrid[i][j] == 1:
                    continue
                if i>=1:
                    visit[i][j] += visit[i-1][j]
                if j>=1:
                    visit[i][j] += visit[i][j-1]
        print(visit)
        return visit[len_y-1][len_x-1]
