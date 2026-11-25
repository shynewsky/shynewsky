# 1. sort() 메서드

def solution(my_string):
    my_list = list(my_string.lower())
    my_list.sort()
    return ''.join(my_list)

# 2. sorted() 함수
# sorted()를 사용하면 한줄로 적을 수 있다

def solution(my_string):
    return ''.join(sorted(my_string.lower()))


