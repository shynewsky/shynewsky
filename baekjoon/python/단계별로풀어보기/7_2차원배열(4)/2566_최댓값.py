matrix = [list(map(int, input().split())) for _ in range(9)]

max_val = 0
max_x = 0
max_y = 0
for i in range(9):
    for j in range(9):
        if max_val < matrix[i][j]:
            max_val = matrix[i][j]
            max_x = i
            max_y = j

print(max_val)
print(max_x + 1, max_y + 1)
