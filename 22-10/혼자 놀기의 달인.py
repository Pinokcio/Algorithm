def solution(cards):
    dic = {}
    for e, i in enumerate(cards):
        dic[i] = e+1
    length = len(cards)
    isVisit = [0 for _ in range(length+1)]
    li = []
    for i in range(1, length+1):
        cur = i
        cnt = 0
        while isVisit[cur]!=1:
            isVisit[cur] = 1
            cnt += 1
            cur = dic[cur]
        li.append(cnt)
    s = sorted(li)
    if len(s) == 1:
        return 0
    return s[-1] * s[-2]
    
#사이클이 만들어지면 상자 열기를 멈춤
#만약 사이클 없이 모든 상자를 열면 0점
#1번그룹, 2번그룹 따로 상자 열기를 해서 각 열은 상자의 수를 곱한 값이 점수가 됨
#이 때, 최고점수를 구하는 문제
