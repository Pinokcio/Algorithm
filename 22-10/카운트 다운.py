def solution(target):
    li = []
    for i in range(60, 0, -1):
        if (1<=i<=20) or (i%2==0 and 1<=i//2<=20) or (i%3==0 and 1<=i//3<=20) or (i==50):
            li.append(i)
    st = set(li) #한번에 접근 가능한 점수
    sb = set(range(1, 21)) 
    sb.add(50) #single / bul이 추가되는 점수
    dp = [[0, 0] for i in range(max(61, target+1))]

    for i in range(1, 61):
        a = 1 if i in st else 2
        b = 0
        if a == 1:
            if i in sb:
                b = 1
            else:
                b = 0
        else:
            cnt = 1
            mina, maxb = [987654321, -1]
            while i-cnt >= 1 and cnt <= 20:
                if mina > dp[i-cnt][0]: 
                    mina = dp[i-cnt][0]
                    maxb = dp[i-cnt][1]
                elif mina >= dp[i-cnt][0] and maxb <= dp[i-cnt][1]:
                    mina = dp[i-cnt][0]
                    maxb = dp[i-cnt][1]
                cnt += 1
            if i-50 >= 1:
                if mina > dp[i-50][0]: 
                    mina = dp[i-50][0]
                    maxb = dp[i-50][1]
                elif mina >= dp[i-50][0] and maxb <= dp[i-50][1]:
                    mina = dp[i-50][0]
                    maxb = dp[i-50][1]
            if mina != 987654321 and maxb != -1: # sb에 있는 수에서 갱신됨
                a = mina+1
                b = maxb+1
            else:
                a = mina+1
                b = maxb
        dp[i] = [a, b]
    for i in range(61, target+1):
        cnt = 1
        mina, maxb = [987654321, -1]
        idx = -1
        while i-cnt >= 1 and cnt <= 60:
            if mina > dp[i-cnt][0] + dp[cnt][0]:
                mina = dp[i-cnt][0] + dp[cnt][0]
                maxb = dp[i-cnt][1] + dp[cnt][1]
            elif mina >= dp[i-cnt][0]+dp[cnt][0] and maxb <= dp[i-cnt][1] + dp[cnt][1]: 
                mina = dp[i-cnt][0] + dp[cnt][0]
                maxb = dp[i-cnt][1] + dp[cnt][1]
            cnt += 1
        dp[i] = [mina, maxb]
    return dp[target]
        
            
#다트는 1~20점이 있고, 더블, 트리플까지 고려할 경우 최대 60점까지 가능
#2 혹은 3의 배수가 아닐 경우에는 더블 혹은 트리플로 안되므로 제외
#싱글과 불을 최대한 맞출 것
#한 번에 가능한 점수들은 li에 넣어둠
#dp로 해결해봄
#dp[i] = [dart, singleORbul] : i점수를 얻는데 필요한 dart수와 그 중 single 또는 bul의 갯수

#1. 최소1부터 최대60점까지의 점수를 한 번에 얻을 수 있기 때문에 해당 범위의 dp를 먼저 계산함
#2. 현재 idx부터 -60에 해당하는 범위를 매번 살펴 그중 dp[idx-cnt][0]+dp[cnt][0]이 최소, dp[idx-cnt][1]+dp[cnt][1]이 최대가 되는 값을 구해서 dp[idx]에 갱신해준다.
