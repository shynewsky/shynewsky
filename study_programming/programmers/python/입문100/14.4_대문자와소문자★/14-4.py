# 1. if문

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()

    return answer

# 2. join()

def solution(my_string):
    return ''.join(i.upper() if i.islower() else i.lower() for i in my_string)

# 3. swapcase()

def solution(my_string):
    return my_string.swapcase()

