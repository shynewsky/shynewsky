N = int(input())
arr = list(map(int, input().split()))
count = 0

for a in arr:
    factors = []
    for i in range(1, a+1):
        if a % i == 0:
            factors.append(i)
    if len(factors) == 2:
        count += 1

print(count)
