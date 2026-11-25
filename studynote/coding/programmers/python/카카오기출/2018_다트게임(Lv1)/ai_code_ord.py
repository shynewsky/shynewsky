def solution(dartResult):
    points = [] # 각 기회(총 3번)의 점수를 저장할 리스트
    i, n = 0, len(dartResult)

    while i < n:
        num = 0
        while i < n and dartResult[i].isdigit():
            # str(dartResult[i]) 대신 ord('0')==48을 이용한 빠른 정수화.
            num = num * 10 + (ord(dartResult[i]) - 48)
            i += 1

        bonus = dartResult[i]
        i += 1
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        else:  # 'T'
            num **= 3

        if i < n and dartResult[i] in '*#':
            opt = dartResult[i]
            i += 1
            if opt == '*':
                if points:
                    points[-1] *= 2
                num *= 2
            else:  # '#'
                num *= -1

        points.append(num)

    return sum(points)
