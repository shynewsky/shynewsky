# 1. 리스트 슬라이싱

def solution(my_string):
    return my_string[::-1]

# 2. reversed() 함수

def solution(my_string):
    return ''.join(reversed(my_string))

# 3. 반복문

def solution(my_string):
    answer = ''
    for str in my_string :
        answer = str + answer
    return answer

# 4. 재귀함수

def solution(my_string):
    first_char = my_string[0]

    # 종료조건
    if len(my_string) == 1:
        return first_char

    # 재귀 조건
    return solution(my_string[1:]) + first_char

