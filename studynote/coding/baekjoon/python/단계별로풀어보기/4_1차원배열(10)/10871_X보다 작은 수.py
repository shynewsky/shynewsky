N, X = map(int, input().split())
arr = list(map(int, input().split()))

print(*[a for a in arr if a < X])
