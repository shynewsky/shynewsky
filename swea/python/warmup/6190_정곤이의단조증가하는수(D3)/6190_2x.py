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
    arr_dan = []
    for i in range(N-1): # arr의 기준점
        for j in range(i+1, N): # arr의 비교점
            num = arr[i] * arr[j]  # 8
            string = str(num)      # '8'
            if list(string) == sorted(string): # 문자열도 sorted() 할 수 있다
                arr_dan.append(num)

    print(f'#{test_case}', max(arr_dan) if arr_dan else -1)
