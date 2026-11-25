M = int(input())
N = int(input())

prime = []
for num in range(M, N+1):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 2:
        prime.append(num)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
