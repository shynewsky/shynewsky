import sys
sys.stdin = open('input.txt')

# 입력 ---------------------------------------------------------------
T = int(input()) # 테스트케이스
for t in range(1, T+1):
    N = int(input()) # N 당근개수 (5<=N<=1000)
    arr = list(map(int, input().split())) # 당근크기 (1<=Ci<=10)

    # 코드 -----------------------------------------------------------
    length = 1
    max_len = 0
    for i in range(1, N):
        if arr[i-1] < arr[i]:
            length += 1
        else:
            length = 1
        if max_len < length:
            max_len = length

    # 출력 -----------------------------------------------------------
    print(f'#{t}', max_len)
