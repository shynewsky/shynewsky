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
    pivot = array[start]
    left = start + 1
    right = end

    while True:
        while left <= right and array[left] < pivot: # 큰 값 찾을때까지
            left += 1
        while right >= left and array[right] > pivot: # 작은 값 찾을때까지
            right -= 1

        if left > right: # 교차하면 종료
            break
        else: # 교차할때까지 자리교환
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    array[start], array[right] = array[right], array[start] # 피벗을 right 와 교환
    return right

# ------------------------------------------------------------------

# 호어 파티션 방식
def partition_hoare(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        while left <= end and arr[left] < pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[start], arr[right] = arr[right], arr[start]
    return right

# -------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)

    print(arr)
