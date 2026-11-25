N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
arr1 = [(a/M*100) for a in arr]
print(sum(arr1)/len(arr1))
