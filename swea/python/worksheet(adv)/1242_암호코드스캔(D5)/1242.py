import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 --------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    # N행 M열 (1<=N<=2000, 1<=M<=500)
    N, M = map(int, input().split())
    # 16진수 M개씩 N줄 -> 2진수로 변환 후
    len = '0' + str(M*4) + 'b'
    data = [''.join(f"{bin(int(input(), 16))[2:]}") for _ in range(N)]

    # 코드 -------------------------------------------------------------

    pprint(len)
    pprint(data)


