import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 -------------------------------------------------------
N = int(input()) # 색종이 수 (1<=N<=100)
data = [list(map(int, input().split())) for _ in range(N)]

# 코드 --------------------------------------------------------
dict = {i : [] for i in range(N)}
for n in range(N):
    x, y, w, h = data[n] # 좌하단 좌표(행렬로 치면 좌상단 좌표), 너비, 높이
    for i in range(x, x+w):
        for j in range(y, y+h):
            for m in range(N-1): # 다른 리스트에 있으면
                if (i,j) in dict[m]:
                    dict[m].remove((i,j))
            dict[n].append((i, j))

for n in range(N):
    print(len(dict[n]))
