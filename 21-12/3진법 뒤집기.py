from collections import deque
def solution(n):
    q = deque()
    div, mod = divmod(n, 3)
    print(div, mod)
    while div != 0:
        q.append(mod)
        div, mod = divmod(div, 3)
    q.append(mod)
    length = len(q)
    sum = 0
    for i in range(0, length):
        sum += q.pop()*pow(3, i)
    return sum
