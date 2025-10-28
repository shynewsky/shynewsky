import sys
sys.stdin = open('input.txt')


# 입력 ---------------------------------------
T = int(input()) # 수확횟수
for t in range(1, T+1):
    N = int(input()) # 당근개수 (3<=N<=1000)
    C = list(map(int, input().split())) # 당근크기 (1<=Ci<=30)

