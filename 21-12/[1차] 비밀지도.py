def solution(n, arr1, arr2):
    answer = [[' ']*n for i in range(0,n)]
    str1 = []
    str2 = []
    for i in range(0, n):
        str1.append('0'*(n-len(bin(arr1[i])[2:])) + bin(arr1[i])[2:])
        str2.append('0'*(n-len(bin(arr2[i])[2:])) + bin(arr2[i])[2:])
    res = []
    for i in range(0, n):
        for j in range(0, n):
            if str1[i][j] == '0' and str2[i][j] == '0':
                answer[i][j] = " "
            else:
                answer[i][j] = "#"
        res.append("".join(answer[i]))
    return res
