# 오름차순으로 정렬한 뒤, 가장 큰 변을 기준으로 비교한다

def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2] :
        return 1
    else :
        return 2
