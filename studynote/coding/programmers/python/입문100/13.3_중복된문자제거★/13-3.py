# 1. 반복문

def solution(my_string):
    answer = []
    for char in my_string:
        if char not in answer:
            answer.append(char)

    return ''.join(answer)

# 2. dict.fromkeys()

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

