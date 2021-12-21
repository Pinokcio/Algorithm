def solution(dartResult):
    answer = 0
    cur = 0
    bef = 0
    flag = 1
    for i in dartResult:
        if i == "S":
            cur = pow(cur,1)
            flag = 1
        elif i == "D":
            cur = pow(cur,2)
            flag = 1
        elif i == "T":
            cur = pow(cur,3)
            flag = 1
        elif i == "*":
            cur *= 2
            answer += bef
            flag = 1
        elif i == "#":
            cur *= -1
            flag = 1
        else :
            if flag == 0:
                cur = 10
            else:
                answer += cur
                bef = cur
                cur = int(i)
                flag = 0
    answer += cur
    return answer
