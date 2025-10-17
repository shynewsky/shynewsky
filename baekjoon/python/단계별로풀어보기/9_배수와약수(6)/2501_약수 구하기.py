N, K = map(int, input().split())
factors = [i for i in range(1, N+1) if N % i == 0]
print(factors[K-1] if len(factors) >= K else 0)
