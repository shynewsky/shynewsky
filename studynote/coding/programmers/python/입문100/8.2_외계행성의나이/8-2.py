# 문자열도 인덱싱 접근이 가능하다

def solution(age):
    num = 'abcdefghij'
    return ''.join(num[int(i)] for i in str(age))
