# 시간초과

import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 정수 개수
    arr = list(map(int, input().split())) # [2, 4, 7, 10]

    # 풀이
    # Ai * Aj 를 구해서 차례대로 담은 배열 만들기
    # [[8], [1, 4], [2, 0], [2, 8], [4, 0], [7, 0]]
    arr_mul = [list(map(int, str(arr[i] * arr[j]))) for i in range(N-1) for j in range(i+1, N)]

    # arr_mul 에서 '단순하게 증가하는 수'인 수를 고른다
    # [8, 14, 28]
    arr_dan = [int(''.join(map(str, i))) for i in arr_mul if i == sorted(i)]

    print(f'#{test_case}', max(arr_dan) if arr_dan else -1)