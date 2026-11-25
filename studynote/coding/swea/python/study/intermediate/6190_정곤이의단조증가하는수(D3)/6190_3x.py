# 오류

import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))
    # 변수
    max_num = 0
    arr2 = sorted([arr[i]*arr[j] for i in range(N) for j in range(i+1, N)])
    # 풀이
    for a in arr2:
        last_digit = ''
        for s in str(a):
            if last_digit == '':
                last_digit = s
            elif int(last_digit) <= int(s): # 단조증가
                last_digit = s
            else: # 단조증가가 아니면 중단
                break
        else:
            max_num = a
    # 출력
    print(f'#{t}',max_num)
