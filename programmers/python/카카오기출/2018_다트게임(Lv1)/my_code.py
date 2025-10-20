def solution(dartResult):
    points = [0] * 3
    darts = []
    n = len(dartResult)

    # 문자열 쪼개기
    start, end = 0, 1
    while start < n:
        if dartResult[start].isdigit() and dartResult[end].isdigit():
            end += 1
        else:
            darts.append(dartResult[start:end])
            start = end
            end += 1
            
    # 점수 계산
    idx = -1
    dict = { 'S':1, 'D':2, 'T':3, }
    for dart in darts:
        if dart.isdigit():
            idx += 1
            points[idx] = int(dart)
        if dart in 'SDT':
            points[idx] **= dict[dart]
        if dart == '*':
            if idx == 0:
                points[0] *= 2
            else:
                points[idx-1] *= 2
                points[idx] *= 2
        if dart == '#':
            points[idx] *= -1

    return sum(points)
