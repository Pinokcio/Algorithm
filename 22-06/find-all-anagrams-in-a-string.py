from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_p = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        dic_s = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        for i in p:
            dic_p[i] += 1
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []
        ans = []
        for i in range(len(p)):
            dic_s[s[i]] += 1
        if dic_s == dic_p:
            ans.append(0)
        for i in range(len_s-len_p):
            dic_s[s[i]] -= 1
            dic_s[s[i+len_p]] += 1
            if dic_s == dic_p:
                ans.append(i+1)
        return ans
