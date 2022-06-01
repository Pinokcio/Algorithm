class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxn = 0
        for n in nums:
            if n == 0:
                cnt = 0
            else:
                cnt += 1
                maxn = max(maxn, cnt)
        return maxn
