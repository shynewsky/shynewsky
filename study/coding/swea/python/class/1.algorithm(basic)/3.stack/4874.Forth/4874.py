# 후위표기법 계산
def evaluate_postfix(arr):

    stack = []

    for a in arr:

        if a == '.':
            if len(stack) > 1:
                return 'error'
            return int(stack.pop())

        elif a.isdigit(): # 피연산자는 무조건 stack에 추가
            stack.append(int(a))
        else: # 연산자는 ㅡ 피연산자 2개 꺼내서 연산후, 결과를 stack에 추가

            if len(stack) < 2:
                return 'error'

            n2 = stack.pop()
            n1 = stack.pop()

            if a == '+':
                stack.append(n1+n2)
            elif a == '-':
                stack.append(n1-n2)
            elif a == '*':
                stack.append(n1*n2)
            elif a == '/':
                if n2 == 0 :
                    return 'error'
                stack.append(n1/n2)
            else:
                return 'error'
    else:
        return 'error'


T = int(input())
for test_case in range(1, T+1):
    data = list(input().split())
    data1 = evaluate_postfix(data)

    print(f'#{test_case}', data1)

    # 발생할 수 있은 오류사항
    # - 연산자를 만났는데, 피연산자가 1개 이하인 경우
    # - . 을 만났는데, 결과값이 2개 이상인 경우
    # - . 이 없는 경우
    # - 0 으로 나누는 경우
    # - 정의되지 않은 연산자가 있는 경우

