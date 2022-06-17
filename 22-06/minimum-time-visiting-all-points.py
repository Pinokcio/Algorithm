import math
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            x = abs(points[i+1][0] - points[i][0])
            y = abs(points[i+1][1] - points[i][1])
            minn = min(x, y)
            ans += minn
            ans += (max(x, y) - minn)
        return ans
