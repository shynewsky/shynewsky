# 1) 반복문 방식
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    prev = None

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            if prev == 'L':
                return False
            right = mid - 1
            prev = 'L'
        else:
            if prev == 'R':
                return False
            left = mid + 1
            prev = 'R'
    return False

# -------------------------------------

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 이진탐색은 반드시 정렬 되어있어야 한다
    A.sort()
    count = 0
    for b in B:
        if binary_search(A, b):
            count += 1
    print(f'#{t}', count)

