from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cul = nums[:]
        dic = {} #nums의 element n의 가장 최근 인덱스
        for i in range(1, len(cul)):
            cul[i] += cul[i-1]
        ans = 0
        idx = -1
        for i in range(len(nums)):
            if nums[i] in dic:
                idx = max(dic[nums[i]], idx)
                ans = max(ans, cul[i] - cul[idx])
                dic[nums[i]] = i
            else:
                dic[nums[i]] = i
                if idx == -1:
                    ans = max(ans, cul[i])
                else:
                    ans = max(ans, cul[i] - cul[idx])
        return ans
"""
지우는 subarray의 elements는 unique하며 최대가 돼야함
0~length까지 하나씩 순차적으로 검사하면서 
  1. 현재값에 대해 이전에 겹치는 값이 존재하는가
    o : 존재한다면 그 이전의 값 인덱스는 몇인가
    x : 존재하지 않으면 2번을 적용
  2. 가장 최근에 겹친 값의 인덱스는 몇인가
  1과 2를 비교하여 현재로부터 비교적 최근에 발생한(인덱스의 값이 더 큰)값까지의 누적을 현재까지의 누적으로부터 뺀다.
위 과정의 최댓값을 구한다.
"""
