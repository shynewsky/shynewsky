# top 활용 

import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):

    text = input()
    length = len(text)

    top = -1
    stack = [0] * length

    ans = 1 # 에러가 없다는 전제

    for char in text : # string 을 순회

        if char == '(' : # 열린 괄호 ㅡ 추가
            top += 1
            stack.append(char)
            # stack[top] = char

        elif char == ')' : # 닫힌 괄호

            if top == -1 : # 첫 괄호가 닫힌 괄호인 경우
                ans = -1   # 잘못된 괄호 짝
                break

            else :           # 앞에 여는 괄호가 있었으면
                top -= 1
                stack.pop() # 여는 괄호 하나 짝지어서 버리기
                # print(stack[top+1])


    if top != -1 : # 짝지어서 지웠는데도, 하나가 남은 경우 (남은 하나는 열림)
        ans = -1

    print(ans)

