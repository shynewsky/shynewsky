def quick_sort(array, start, end):
    if start < end:
        pivot_idx = partition(array, start, end)
        quick_sort(array, start, pivot_idx-1)
        quick_sort(array, pivot_idx+1, end)

def partition(array, start, end):
    pivot = array[start]
    left = start+1
    right = end
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] > pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[start], array[right] = array[right], array[start]
    return right

# -------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(f'#{t}', arr[len(arr)//2])