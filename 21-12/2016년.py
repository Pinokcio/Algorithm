def solution(a, b):
    answer = ''
    dic = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dic2 = {0 : "FRI", 1:"SAT", 2:"SUN", 3:"MON", 4:"TUE", 5:"WED", 6:"THU"}
    sum = 0
    for i in range(1, a):
        sum += dic[i]
    sum += (b-1)
    answer = dic2[sum%7]
    return answer
