import math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        nums.sort()
        res = math.inf
        if length % 2 == 0:
            ans = 0
            for i in range(length):
                ans += abs(nums[i] - nums[length//2-1])
            res = min(res, ans)
            ans = 0
            for i in range(length):
                ans += abs(nums[i] - nums[length//2])
            res = min(res, ans)
            return res
        else:
            ans = 0
            for i in range(length):
                ans += abs(nums[i] - nums[length//2])
            res = min(res, ans)
            return res
