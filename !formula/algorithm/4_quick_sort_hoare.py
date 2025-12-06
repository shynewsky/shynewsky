'''
3 2 4 6 9 1 8 7 5
p l →         ← r
p : 첫번째 값을 피벗으로 선택
l : 두번째 값을 왼끝으로 선택, 시작점 포함 p 이상 값 찾기
r : 마지막 값을 오른끝으로 선택, 시작점 포함 p 이하 값 찾기

3 2 4 6 9 1 8 7 5
p   l  ↔  r
l이 지나간 길은 모두 p 미만 값 (2)
r이 지나간 길은 모두 p 초과 값 (5 7 8)

3 2 1 6 9 4 8 7 5
p ↔ r     l
l이 지나간 길 + r이 찾은 값 = p 이하 값
r 뒷쪽으로 p를 이동해서 다시 검색한다

1 2 3 6 9 4 8 7 5
r   p     l
p의 왼쪽으로 모두 p보다 작은 값
p의 오른쪽은 아직 모두 p보다 큰지 확신할 수 없음

'''

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start+1  # pivot 이상 값 찾을때까지 오른쪽으로 이동
    right = end     # pivot 이하 값 찾을때까지 왼쪽으로 이동

    while True:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and pivot < arr[right]:
            right -= 1

        if right < left: # 교차하면
            break
        else: # 교차할때까지 계속 자리교환
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr[start], arr[right] = arr[right], arr[start]
    return right

quick_sort(arr, 0, len(arr)-1)
print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
