# 방1)
# 시간초과

import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T+1):

    # 입력
    X = int(input())

    # 변수
    x, y = [0, 0] # 시작좌표
    delta = [[-1, 1], [1, -1]] # 우상향, 좌하향
    d = 0
    count = 1

    while count != X:

        dx, dy = delta[d%2] #
        nx, ny = x + dx, y + dy

        # 범위 밖을 벗어나면
        if not (0<=nx and 0<=ny):
            if (d%2) == 1:
                nx, ny = x + 1, y
                d += 1
            elif (d%2) == 0:
                nx, ny = x, y + 1
                d += 1

        x, y = nx, ny
        count += 1

    print(f'{x+1}/{y+1}')

# 방2) ㄱㄷㅇ님
# ⭐다음 층수의 범위 끝을 구해서 비교해라⭐

import sys
sys.stdin = open('input.txt')

N = int(input())
floor = 1
floor_min = 1
floor_max = 1

# 다음층 시작범위 = 현재층 시작범위 + 현재층 층수
# 다음층 끝범위 = 현재층 끝범위 + 다음층수
while floor_max < N:
    floor_min += floor
    floor += 1
    floor_max += floor

# 짝수층이면 정순, 홀수층이면 역순
if floor%2 == 0:
    print(f'{N - floor_min + 1}/{floor - (N - floor_min)}')
elif floor%2 == 1:
    print(f'{floor - (N - floor_min)}/{N - floor_min + 1}')


