def solution(sizes):
    N = len(sizes)
    max_width = 0
    max_height = 0
    for i in range(N):
        sizes[i] = sorted(sizes[i])
        if max_width < sizes[i][0]:
            max_width = sizes[i][0]
        if max_height < sizes[i][1]:
            max_height = sizes[i][1]
    return max_width * max_height
