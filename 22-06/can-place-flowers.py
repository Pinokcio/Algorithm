from collections import deque
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        q = deque(flowerbed)
        q.appendleft(0)
        q.append(0)
        for i in range(1, len(q)-1):
            if q[i-1] == q[i] == q[i+1] == 0:
                q[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
