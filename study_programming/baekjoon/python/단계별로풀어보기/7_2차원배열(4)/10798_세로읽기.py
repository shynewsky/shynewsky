arr = [list(input().strip()) for _ in range(5)]

max_len = 0
for a in arr:
    if max_len < len(a):
        max_len = len(a)

for a in arr:
    while max_len != len(a):
        a.append('')

matrix = list(zip(*arr))
print(''.join([char for row in matrix for char in row]))
