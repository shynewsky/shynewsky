# 방1)
#시간 초과

# N이 K층에 있을때 ㅡ 3*(K-2)*(K-1)+1 < N <= 3*(K-1)*K+1
N = int(input())
K = 0
while True:
    if 3*(K-2)*(K-1)+1 < N <= 3*(K-1)*K+1 :
        print(K)
        break
    K += 1

# 방2) ㄱㄷㅇ님
# ⭐다음 층수의 범위 끝을 구해서 비교해라⭐

import sys
sys.stdin = open('input.txt')

N = int(input())
floor = 1
floor_max = 1

# 다음 층 끝범위 = 현재층 끝범위 + 6 * (현재층수-1)
# 현재 층수를 갱신하기 전에, 다음 층 끝범위를 구하고, 다음 층으로 갱신한다
while floor_max < N: # 끝범위가 N보다 커질때까지 돌린다
    floor_max += 6 * floor  # 다음 층수의 최고 끝 범위를 구하고
    floor += 1              # 다음 층으로 이동한다

print(floor)
