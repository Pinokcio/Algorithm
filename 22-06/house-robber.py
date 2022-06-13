class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        res = [[0,0] for _ in range(length)]
        res[0] = [0, nums[0]]
        for i in range(1, length):
            res[i][0] = max(res[i-1])
            res[i][1] = max(res[i-1][0]+nums[i], res[i-1][1])
        return max(res[-1])
