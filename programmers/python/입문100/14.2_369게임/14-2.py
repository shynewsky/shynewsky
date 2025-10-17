# 1. count 올리기

def solution(order):

    count = 0
    for i in str(order):
        if i in '369':
            count += 1

    return count

# 2. sum() 사용하기

def solution(order):
    return sum(1 for i in str(order) if i in '369')
