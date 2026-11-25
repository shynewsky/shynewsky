# 딕셔너리를 사용하지 않으면, 메모리 사용량은 줄지만, 코드는 복잡해진다
# 1/0 대신 T/F 을 사용하면, 메모리 사용량이 조금 더 크다

import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1) :

    # 입력
    arr = input()
    N = len(arr)

    # 열린 괄호의 경우에는 상관없이 stack 에 넣지만
    # 닫힌 괄호의 경우에는, 짝이 맞는 열린 괄호를 pop() 시켜야한다

    # 짝 매칭을 위한 닫힌 괄호
    diction = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    # 스택 준비

    # 방1) 채워진 스택을 만들거면 stack[top] = value
    # top = -1
    # stack = [0] * N

    # 방2) 빈 스택을 만들거면 append(), pop() 사용
    stack = []

    # 성공하면 True, 실패하면 False
    ans = True

    # 스택

    for char in arr : # 문자열 순회

        if char in '({[' : # 열린 괄호면 무조건 추가
            stack.append(char)

        elif char in ')}]' : # 닫힌 괄호면, 짝이 되는 열린 괄호를 삭제

            if len(stack) == 0 : # 열린 괄호가 아무것도 없으면
                ans = False 
                
            elif stack[-1] == diction[char]:
                stack.pop()

            else :
                ans = False

    if len(stack) != 0 :
        ans = False

    print(f'#{test_case} {int(ans)}')

