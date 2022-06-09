class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for e, i in enumerate(numbers):
            if target - i in dic:
                return [dic[target-i], e+1]
            else:
                dic[i] = e+1
