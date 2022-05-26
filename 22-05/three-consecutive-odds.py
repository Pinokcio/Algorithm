class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        f1, f2, f3 = 0, 0, 0
        if arr[0] % 2 == 1:
            f1 = 1
        if arr[1] % 2 == 1:
            f2 = 2
        for i in range(2, length):
            f3 = 1 if arr[i] % 2 == 1 else 0
            if f1 and f2 and f3:
                return True
            f1 = f2
            f2 = f3
        return False
