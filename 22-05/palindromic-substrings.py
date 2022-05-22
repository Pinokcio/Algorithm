class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        cnt = 0
        for i in range(length):
            start = i-1
            end = i+1
            cnt += 1
            while 0<=start and end<length:
                if s[start] == s[end]:
                    cnt += 1
                    start -= 1
                    end +=1 
                else:
                    break
        
        for i in range(length-1):
            if s[i] == s[i+1]:
                start = i-1
                end = i+2
                cnt += 1
                while 0<=start and end<length:
                    if s[start] == s[end]:
                        cnt += 1
                        start -= 1
                        end +=1 
                    else:
                        break
        return cnt
        
