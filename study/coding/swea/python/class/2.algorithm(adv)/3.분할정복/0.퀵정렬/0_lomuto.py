import sys
sys.stdin = open('input.txt')

# hoare 가 lomuto 보다 효율적이다

# 정렬하는 함수 (공통) --------------------------------------------
def quick_sort(array, start, end):
    if start < end:
        pivot_idx = partition(array, start, end) # 피벗고정
        quick_sort(array, start, pivot_idx - 1) # 왼쪽정렬
        quick_sort(array, pivot_idx + 1, end) # 오른쪽정렬

# ------------------------------------------------------------------

# 피벗 고정하는 함수
def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            if i != j :
                array[i], array[j] = array[j], array[i]
    
    if (i+1) != end:
        array[i+1], array[end] = array[end], array[i+1]
        
    return i+1

# ------------------------------------------------------------------

# 로무토 파티션 방식
def partition_hoare(arr, start, end):
    pivot = arr[end]
    i = low - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

# -------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)

    print(arr)
