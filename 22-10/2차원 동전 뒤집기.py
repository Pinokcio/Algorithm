def solution(beginning, target):
    answer = 0
    answer_tmp = 0
    len_y = len(beginning)
    len_x = len(beginning[0])
    diff_mat = [[0 for _ in range(len_x)] for _ in range(len_y)]
    diff_mat_tmp = [[0 for _ in range(len_x)] for _ in range(len_y)]
    for y in range(len_y):
        for x in range(len_x):
            if beginning[y][x] != target[y][x]:
                diff_mat[y][x] = 1          
                diff_mat_tmp[y][x] = 1
                
    for y in range(len_y):
        if diff_mat[y][0] == 0:
            answer += 1
            for x in range(len_x):
                diff_mat[y][x] = 1 if diff_mat[y][x]==0 else 0
    for x in range(len_x):
        if diff_mat[0][x] == 1:
            answer += 1
            for y in range(len_y):
                diff_mat[y][x] = 1 if diff_mat[y][x]==0 else 0
                
    
    for y in range(len_y):
        if diff_mat_tmp[y][0] == 1:
            answer_tmp += 1
            for x in range(len_x):
                diff_mat_tmp[y][x] = 1 if diff_mat_tmp[y][x]==0 else 0
    for x in range(len_x):
        if diff_mat_tmp[0][x] == 1:
            answer_tmp += 1
            for y in range(len_y):
                diff_mat_tmp[y][x] = 1 if diff_mat_tmp[y][x]==0 else 0       
    
    flag = 0
    for d in diff_mat:
        for i in d:
            if i == 1:
                flag = 1
    for d in diff_mat_tmp:
        for i in d:
            if i == 1 and flag == 1:
                return -1
    return min(answer, answer_tmp)

#경우에 따라서 matrix[0][0]은 double check되기 때문에 처음에 0을 뒤집는 경우, 뒤집지 않는 경우 두가지에 대해서 계산함
