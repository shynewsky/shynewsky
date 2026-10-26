# 방1)
# 인덱스번호 = 10진법
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = input().split()
B = int(B)

e = 0
total = 0
for char in reversed(N): # 뒤에서부터 거꾸로 돌면서
    total += (B ** e) * arr.index(char)
    e += 1

print(total)

# 방2)

N, B = input().split()
print(int(N, int(B)))
