dots3 = [list(map(int, input().split())) for _ in range(3)]

x_set = set()
y_set = set()
for x, y in dots3:
    x_set.add(x)
    y_set.add(y)

dots4 = [[x, y] for x in x_set for y in y_set]

for dot in dots4:
    if dot not in dots3:
        print(*dot)
