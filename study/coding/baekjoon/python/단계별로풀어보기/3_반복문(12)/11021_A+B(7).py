# 방1)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')

# 방2) ㄱㅁㅈ님

import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    sum_t = A+B
    print(f'Case #{tc}: {sum_t}')
