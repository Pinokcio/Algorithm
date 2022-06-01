from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q = deque()
        ans = []
        for i in s:
            if i == '(':
                q.append('(')
                ans.append('(')
            elif i == ')':
                if q:
                    q.popleft()
                    ans.append(')')
            else:
                ans.append(i)
        res = []
        q = deque()
        for a in ans[::-1]:
            if a == ')':
                q.append(')')
                res.append(')')
            elif a == '(':
                if q:
                    q.popleft()
                    res.append('(')
            else:
                res.append(a)
                
        return "".join(res[::-1])
