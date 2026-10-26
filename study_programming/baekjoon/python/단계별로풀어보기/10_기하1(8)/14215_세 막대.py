arr = sorted(list(map(int, input().split())))
if arr[0]+arr[1] <= arr[2]:
    arr[2] = arr[0]+arr[1]-1
print(sum(arr))

