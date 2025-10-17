def solution(rsp):
    answer = ''
    for char in rsp :
        if char == '0' : answer += '5'
        elif char == '2': answer += '0'
        else : answer += '2'
    return answer
