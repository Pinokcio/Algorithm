from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter()
        target = len(nums)//3
        for n in nums:
            counter[n] += 1
        res = []
        for c in counter:
            if counter[c] > target:
                res.append(c)
        return res
