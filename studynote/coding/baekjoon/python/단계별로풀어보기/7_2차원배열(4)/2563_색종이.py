N = int(input()) # 색종이수
matrix = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 100 for _ in range(100)]

for x, y in matrix:
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            count += 1

print(count)

