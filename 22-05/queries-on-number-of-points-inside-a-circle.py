class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            cnt = 0
            r2 = q[2]**2
            for p in points:
                if r2 >= ((p[0]-q[0])**2+(p[1]-q[1])**2):
                    cnt += 1
            ans.append(cnt)
        return ans
