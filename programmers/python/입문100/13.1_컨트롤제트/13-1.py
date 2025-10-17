# 1. 반복문

def solution(string):

    str_list = list(string.split())[::-1]
    N = len(str_list)

    idx = 0
    num_list = []

    while idx < N : # 끝까지 갈때까지 진행

        if str_list[idx] != 'Z':
            num_list.append(str_list[idx])
            idx += 1
        else :
            idx += 2

    num_list = [int(i) for i in num_list]
    return sum(num_list)

# 2. 스택

def solution(string):
    stack = []
    for s in string.split():
        if s == 'Z' and stack:
            stack.pop()
        else:
            stack.append(int(s))
    return sum(stack)
