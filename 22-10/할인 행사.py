from collections import defaultdict
def solution(want, number, discount):
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n
    
    dis = defaultdict(int)
    for i in range(10):
        dis[discount[i]] += 1
    length = len(discount)
    res = 0
    for w in want:
        if w not in dis:
            break
        if dic[w] > dis[w]:
            break
    else:
        res += 1
        
    for i in range(10, length):
        dis[discount[i]] += 1
        dis[discount[i-10]] -= 1
        for w in want:
            if w not in dis:
                break
            if dic[w] > dis[w]:
                break
        else:
            res += 1
    return res
