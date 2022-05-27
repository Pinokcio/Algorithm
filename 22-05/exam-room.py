class ExamRoom:
    def __init__(self, n: int):
        self.arr = []
        self.n = n
        self.l = 0
        self.r = 0
        self.length = 0
    def seat(self) -> int:
        if self.arr == []:
            self.arr.append(0)
            self.length += 1
            self.l = 0
            self.r = 0
            return 0
        diff = -1
        idx = -1
        if self.l > diff:
            diff = self.l
            idx = -1
        for i in range(1, self.length):
            if diff < (self.arr[i] - self.arr[i-1])//2 :
                diff = (self.arr[i] - self.arr[i-1])//2
                idx = i-1
        if (self.n-1) - self.r > diff:
            diff = ((self.n-1) - self.r)
            idx = self.length-1
        if idx == -1:
            self.arr.insert(0, 0)
        else:
            self.arr.insert(idx+1, self.arr[idx]+diff)
        self.length += 1
        if self.arr[idx+1] < self.l:
            self.l = self.arr[idx+1]
        if self.arr[idx+1] > self.r:
            self.r = self.arr[idx+1]
        #print('insert : ', self.arr, self.arr[idx+1], diff, self.l, self.r)
        return self.arr[idx+1]

    def leave(self, p: int) -> None:
        self.arr.remove(p)
        self.length -= 1
        if self.length != 0:
            self.l = self.arr[0]
            self.r = self.arr[-1]
        #print('remove : ', self.arr, p, self.l, self.r)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
