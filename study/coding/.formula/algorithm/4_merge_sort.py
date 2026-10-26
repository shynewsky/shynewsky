'''
3 2 5 0 1 8 7 6 9 4
3 2 5 0 1 // 8 7 6 9 4
3 2 5 0 1 // 8 7 // 6 9 4
3 2 5 0 1 // 8 7 // 6 // 9 4
3 2 5 0 1 // 8 7 // 6 // 9 // 4
3 2 5 0 1 // 8 7 // 6 // 4 9
3 2 5 0 1 // 8 7 // 4 6 9
3 2 5 0 1 // 8 // 7 // 4 6 9
3 2 5 0 1 // 7 8 // 4 6 9
3 2 5 0 1 // 4 6 7 8 9
3 2 // 5 0 1 // 4 6 7 8 9
3 2 // 5 // 0 1 // 4 6 7 8 9
3 2 // 5 // 0 // 1 // 4 6 7 8 9
3 2 // 5 // 0 1 // 4 6 7 8 9
3 2 // 0 1 5 // 4 6 7 8 9
3 // 2 // 0 1 5 // 4 6 7 8 9
2 3 // 0 1 5 // 4 6 7 8 9
0 1 2 3 5 // 4 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):

    merged = []
    left_idx, right_idx = 0, 0
    left_len, right_len = len(left), len(right)

    while left_idx < left_len and right_idx < right_len:
        
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged
