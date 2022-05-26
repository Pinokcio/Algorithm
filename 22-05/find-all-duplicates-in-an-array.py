class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for n in nums:
            if n in dic:
                res.append(n)
            else:
                dic[n] = 1
                
        return res
