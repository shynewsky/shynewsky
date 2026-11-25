import sys
sys.stdin = open('input.txt')

T = 10 # 테스트 케이스

for test_case in range(1, T+1) :

    # 입력
    N = int(input()) # 문자 길이
    arr = list(input())

    # 딕셔너리 - Value인지 파악하고 pop()
    diction = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
        '>' : '<',
    }

    # 스택
    stack = []
    ans = 1

    for ele in arr : # 글자 하나씩 순회

        if ele in '({[<' : # 열린 괄호일때 ㅡ 무조건 추가
            stack.append(ele)

        elif ele in ')}]>' : # 닫힌 괄호일때 ㅡ 추가 / 소거

            if stack[-1] == diction[ele] : # 마지막 원소가 짝꿍일때 ㅡ 소거
                stack.pop()

            else :
                stack.append(ele)

    if len(stack)!= 0 :
        ans = 0

    print(f'#{test_case} {ans}')

