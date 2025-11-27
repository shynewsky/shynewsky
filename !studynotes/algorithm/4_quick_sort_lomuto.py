'''
3 2 4 6 9 1 8 7 5
                p
j               i
p : 마지막 값을 피벗으로 설정
i : start-1 이므로 오른끝=피벗위치 로 초기화된다
j : 실질적으로 배열을 순회 - p 이상 값 찾을때까지 자리 바꾸며 오른쪽으로 이동

                p
3 2 4 6 9 1 8 7 5
j                 (j < p)
i                 (j == i+1)
3 2 4 6 9 1 8 7 5
  j               (j < p)
  i               (j == i+1)
3 2 4 6 9 1 8 7 5
    j             (j < p)
    i             (j == i+1)
3 2 4 6 9 1 8 7 5
    j             (j < p)
    i             (j == i+1)
3 2 4 6 9 1 8 7 5
      j           (j > p)
      i           (i+1 ↔ p)
3 2 4 5 9 1 8 7 6
      j
      p         i

'''

def quick_sort(arr, start, end): # 동일
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = arr[end] # 마지막 원소를 피벗으로
    i = start-1      

    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]

    if (i+1) != end:
        arr[end], arr[i+1] = arr[i+1], arr[end]

    return i+1

quick_sort(arr, 0, len(arr)-1)
print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
