class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        arr = [[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        st = set()
        
        for m in mines:
            st.add(tuple(m))
            
        for i in range(n):
            cul = 0
            for j in range(n):
                if (i,j) not in st:
                    cul += 1
                    arr[i][j][0] = cul
                else:
                    cul = 0
        
        for i in range(n-1, -1, -1):
            cul = 0
            for j in range(n-1, -1, -1):
                if (i,j) not in st:
                    cul += 1
                    arr[i][j][1] = cul
                else:
                    cul = 0
        
        for i in range(n):
            cul = 0
            for j in range(n):
                if (j,i) not in st:
                    cul += 1
                    arr[j][i][2] = cul
                else:
                    cul = 0
        
        for i in range(n-1, -1, -1):
            cul = 0
            for j in range(n-1, -1, -1):
                if (j,i) not in st:
                    cul += 1
                    arr[j][i][3] = cul
                else:
                    cul = 0
        maxn = 0
        for i in range(n):
            for j in range(n):
                maxn = max(maxn, min(arr[i][j]))
        return maxn
