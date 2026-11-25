# count()

def solution(array):
    count = 0
    for num in array:
        count += str(num).count('7')
    return count

# 리스트 컴프리헨션

def solution(array):
    return ''.join(map(str, array)).count('7')
