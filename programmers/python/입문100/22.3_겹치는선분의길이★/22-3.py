def solution(lines):
    N = len(lines)
    array = [0] * 201
    for a, b in lines:
        for i in range(a, b):
            array[i + 100] += 1
    count = 0
    for i in array:
        if i > 1:
            count += 1

    return count
