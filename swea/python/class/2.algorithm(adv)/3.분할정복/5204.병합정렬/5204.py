def merge(left_arr, right_arr):
    global comparison_count

    if left_arr and right_arr:
        if left_arr[-1] > right_arr[-1]:
            comparison_count += 1

    merged_arr = []
    left_idx, right_idx = 0, 0
    left_size, right_size = len(left_arr), len(right_arr)

    while left_idx < left_size and right_idx < right_size:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])
    return merged_arr

def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

# ----------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    comparison_count = 0
    arr2 = merge_sort(arr)
    print(f'#{t}', arr2[len(arr2)//2], comparison_count)
