'''
- 반드시 정렬된 상태에서 사용
- 한번 정렬 후, 여러번의 검색ㅇ르 수행할때 유리
'''

#--------------------------------------------------

# 이진검색(반복문)

def binary_search(arr, num):
    left, right = 0, len(arr)-1

    while left <= right:       # right < left 될때까지
        mid = (left + right) // 2
        if arr[mid] == num:    # 중간값으로 바로 찾은 경우
            return mid
        elif num < arr[mid]:   # 왼쪽에 있을 경우
            right = mid-1      # 오른쪽 끝을 당겨온다
        elif arr[mid] < num:   # 오른쪽에 있을 경우
            left = mid+1       # 왼쪽 끝을 당겨온다
    return -1                  # 찾지 못한 경우

arr = [2, 4, 7, 9, 11, 19, 23] # 정렬된 상태에서 사용
idx = binary_search(arr, 9)
print(idx)

#--------------------------------------------------

# 이진검색(재귀)

def binary_search(arr, num, left, right):

    if right < left:           # 종료조건
        return -1

    mid = (left + right) // 2
    if arr[mid] == num:        # 중간값으로 바로 찾은 경우
        return mid
    elif num < arr[mid]:       # 왼쪽에 있을 경우
        return binary_search(arr, num, left, mid-1)
    elif arr[mid] < num:       # 오른쪽에 있을 경우
        return binary_search(arr, num, mid+1, right)
    return -1                  # 찾지 못한 경우

arr = [2, 4, 7, 9, 11, 19, 23] # 정렬된 상태에서 사용
idx = binary_search(arr, 9, 0, len(arr)-1)
print(idx)
