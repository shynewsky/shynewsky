# 1. 리스트슬라이싱

def solution(num_list):
    return num_list[::-1]

# 2. reversed() 함수

def solution(num_list):
    return list(reversed(num_list))

# 3. reverse() 메서드

def solution(num_list):
    num_list.reverse()
    return num_list
