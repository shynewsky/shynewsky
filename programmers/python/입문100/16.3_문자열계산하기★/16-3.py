def solution(my_string):

    arr = list(my_string.split())

    print(arr)

    # 후위 표기법 변환
    stack = [] # 연산자 + -
    result = [] # 피연산자(숫자)
    for a in arr:
        if a.isdigit(): # 피연산자 ㅡ result
            result.append(a)
        else : # 연산자 ㅡ stack에 넣은 것과 비교하여, 기존것은 result 에 옮기고, 새거는 stack에 옮기기
            while stack:
                result.append(stack.pop())
            stack.append(a)

    while stack:
        result.append(stack.pop())

    print(result)

    # 후위표기법 계산
    temp = []
    for a in result:
        if a.isdigit(): # 피연산자 ㅡ temp
            temp.append(int(a))
        else: # 연산자 ㅡ 피연산자 2개 뽑아서 연산후 temp 에 넣기
            n2 = temp.pop()
            n1 = temp.pop()
            if a == '+':
                temp.append(n1+n2)
            elif a == '-':
                temp.append(n1-n2)

    return temp.pop()

print(solution('3 + 4 + 9 - 12'))
