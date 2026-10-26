def recur():

    dp = [0] * N # 1월부터 12월까지
    for i in range(N):
        if i == 0: # 1월이면
            dp[i] = min(arr[i]*A, B, D)
        elif i == 1: # 2월이면
            dp[i] = min(dp[i-1]+(arr[i]*A), dp[i-1]+B, D)
        elif 1 < i < 12 : # 3~11월이면
            dp[i] = min(dp[i-1]+(arr[i]*A), dp[i-1]+B, dp[i-3]+C, D)
        elif i == 12: # 12월이면
            dp[i] = min(dp[i-1]+(arr[i]*A), dp[i-1]+B, dp[i-3]+C, D)
    return dp[-1]

T = int(input())
for t in range(1, T+1):
    # 입력
    A, B, C, D = map(int, input().split())
    arr = list(map(int, input().split()))
    # 변수
    N = len(arr)
    S = sum(arr)
    # 풀이
    min_sum = recur() # 1월부터
    # 출력
    print(f'#{t}', min_sum)
