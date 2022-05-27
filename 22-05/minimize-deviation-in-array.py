import heapq as hq
import math
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxn = max(nums)
        minn = min(nums)
        minheap = []
        maxheap = []
        nums.sort()
        minres = nums[-1] - nums[0]
        
        for n in nums:
            hq.heappush(minheap, n)
        
        n = hq.heappop(minheap)
        while n % 2 == 1:
            maxn = max(maxn, n*2)
            hq.heappush(minheap, n*2)
            n = hq.heappop(minheap)
            minres = min(minres, abs(maxn - n))
        hq.heappush(minheap, n)
        minn = n
        
        for n in minheap:
            hq.heappush(maxheap, -n)
            minn = min(minn, n)
        
        n = -hq.heappop(maxheap)
        while n % 2 == 0:
            minn = min(minn, n//2)
            hq.heappush(maxheap, -(n//2))
            n = -hq.heappop(maxheap)
            minres = min(minres, abs(n - minn))
        
        return minres
