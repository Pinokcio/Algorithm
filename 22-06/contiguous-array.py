class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        cul = [[0, 0] for _ in range(length)]
        dic = {}
        for e,i in enumerate(nums):
            if i == 0:
                cul[e][0] += 1
            else:
                cul[e][1] += 1
        dic[cul[0][0] - cul[0][1]] = 0
        for i in range(1, length):
            cul[i][0] += cul[i-1][0]
            cul[i][1] += cul[i-1][1]
            if cul[i][0] - cul[i][1] == 0:
                dic[0] = i
            elif cul[i][0] - cul[i][1] not in dic:
                dic[cul[i][0] - cul[i][1]] = i
        maxn = 0
        if 0 in dic:
            maxn = dic[0]+1
        for i in range(length-1, -1, -1):
            maxn = max(maxn, i - dic[cul[i][0]-cul[i][1]])
        return maxn
