def solution(arr):
    N = len(arr)
    for i in range(N-1, 0, -1):
        if arr[i] == arr[i-1]:
            arr.pop(i)
    return arr