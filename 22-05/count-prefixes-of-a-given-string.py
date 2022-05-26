class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for w in words:
            length = len(w)
            if length > len(s):
                continue
            for i in range(length):
                if s[i] != w[i]:
                    break
            else:
                cnt += 1
        return cnt
