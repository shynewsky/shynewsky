def solution(n):
    list = []
    for i in str(n) :
        list.append(int(i))
    return sum(list)

# 리스트 컴프리헨션

def solution(n):
    return sum(int(digit) for digit in str(n))
