def recur():
    global min_sum

    total = sum(arr) # 부분합 표시 테이블(bitset처럼 사용)
    dp = [0] * (total+1)
    dp[0] = 1 # 합0은 항상 가능(아무것도 안고를때)

    for i in range(N): # 각 원소를 한번씩 사용해 부분합 갱신
        for j in range(total-arr[i], -1, -1):
            if dp[j]:
                dp[j+arr[i]] = 1

    for s in range(B, total+1):
        if dp[s]:
            min_sum = s
            return

    return

T = int(input())
for t in range(1, T+1):
    # 입력
    N, B = map(int, input().split()) # N명, B높이
    arr = list(map(int, input().split())) # N명
    # 변수
    min_sum = float('inf')
    # 풀이
    recur()
    # 출력
    print(f'#{t}', min_sum-B)