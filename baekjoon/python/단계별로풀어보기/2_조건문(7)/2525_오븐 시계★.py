# 방1)

A, B = map(int, input().split()) # 현재 시각
C = int(input()) # 필요한 시간

A += (B+C) // 60
B = (B+C) % 60

A %= 24

print(A, B)

# 방2)

h, m = map(int, input().split())
t = int(input())

total = (h * 60 + m + t) % (24 * 60)
h, m = divmod(total, 60)
print(h, m)
