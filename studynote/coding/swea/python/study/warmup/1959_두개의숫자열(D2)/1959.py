import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1) :

    # 입력
    N, M = map(int, input().split()) # N개, M개
    A = list(map(int, input().split())) # A 숫자열
    B = list(map(int, input().split())) # B 숫자열

    # 코드
    # 길이가 작은 배열 인덱스에, 숫자를 추가하여 길이가 긴 배열의 인덱스를 만든다
    # 1. '차'가 되는 수를 for 문으로 돌며
    # 2. '작은 배열 인덱스'가 되는 수를 for 문으로 돈다
    # 임의로, 길이가 작은 배열을 A에 두고, 길이가 긴 배열을 B에 둔다

    if N > M : # 받아온 배열 중 A가 더 긴 경우 - A와 B의 자리 교환
        N, M = M, N
        A, B = B, A

    max_sum = 0 # 최댓값
    for i in range(M-N+1) : # 0 이상, N-M 이하 (N-M+1 미만)

        sum_up = 0          # 작은 배열 위치를 이동할때마다 새로운 곱합을 구한다
        for j in range(N) : # A 숫자열 순회
            sum_up += A[j] * B[j+i]

        # 최댓값 구하기
        if max_sum < sum_up :
            max_sum = sum_up

    print(f'#{test_case} {max_sum}')

