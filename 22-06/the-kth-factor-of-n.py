import math
from collections import deque
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        q = deque()
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                if i == n//i:
                    q.append(i)
                else:
                    q.appendleft(i)
                    q.append(n//i)
        print(q)
        if k > len(q):
            return -1
        return q[k-1]
