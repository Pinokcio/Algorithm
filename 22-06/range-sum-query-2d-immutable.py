class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cul = matrix[:]
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.cul[i][j] += self.cul[i][j-1]
        for i in range(len(matrix[0])):
            for j in range(1, len(matrix)):
                self.cul[j][i] += self.cul[j-1][i]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n1 = self.cul[row2][col2]
        n2 = 0
        n3 = 0
        n4 = 0
        if row1 != 0 and col1 != 0:
            n2 = self.cul[row1-1][col1-1]
        if row1 != 0:
            n3 = self.cul[row1-1][col2] 
        if col1 != 0:
            n4 = self.cul[row2][col1-1]
        return n1 + n2 - n3 - n4


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
