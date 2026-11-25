# 1.

def solution(string):
    answer = ''
    for s in string:
        if string.count(f'{s}') == 1:
            answer += s

    return ''.join(sorted(answer))

# 2. 리스트 컴프리헨션

def solution(string):
    return ''.join(sorted([s for s in string if string.count(s) == 1]))
