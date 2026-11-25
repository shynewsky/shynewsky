# 방1)

N = int(input())
ans = 0
for i in range(1, N+1):
    num = digits = i
    while num > 0:
        digits += num % 10
        num //= 10
    if digits == N:
        ans = i
        break
print(ans)

# 방2)

N = int(input())
for i in range(1, N+1):
    if sum(map(int, str(i))) + i == N:
        print(i)
        break
else:
    print(0)



