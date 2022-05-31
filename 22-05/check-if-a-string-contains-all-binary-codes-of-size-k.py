class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(0, len(s)):
            st.add(s[i:i+k])
            if i+k == len(s):
                break
        return True if len(st) == 2**k else False
