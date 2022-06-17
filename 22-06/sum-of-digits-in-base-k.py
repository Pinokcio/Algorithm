class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = []
        while n >= k:
            res.append(n%k)
            n = n//k
        res.append(n)
        return sum(res)
