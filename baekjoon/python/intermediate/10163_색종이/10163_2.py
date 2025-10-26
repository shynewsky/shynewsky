import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 -------------------------------------------------------
N = int(input()) # 색종이 수 (1<=N<=100)
data = [list(map(int, input().split())) for _ in range(N)]

# 코드 --------------------------------------------------------
'''
평면이 1001 * 1001 = 1천만이 넘어가므로, 1초 넘음. 즉, 행렬사용불가
'''
dict = {i : [] for i in range(N)}
for n in range(N-1, -1, -1): # 역순회
    x, y, w, h = data[n] # 좌하단 좌표(행렬로 치면 좌상단 좌표), 너비, 높이
    for i in range(x, x+w):
        for j in range(y, y+h):
            is_element = False
            for m in range(n+1, N):
                if (i,j) not in dict[m]:
            dict[n].append((i, j))



    for l in range(N):
        print(len(dict[n]))

for n in range(N):
    print(len(dict[n]))
