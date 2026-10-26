# 후위표기법 변환
def infix_to_postfix(arr):

    order = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
    }

    stack = [] # 괄호, 연산자
    result = [] # 피연산자, 연산자

    for a in arr:

        if a.isdigit(): # 피연산자 ㅡ 무조건 result
            result.append(a)
        elif len(stack) == 0: # 연산자 ㅡ 첫번째 연산자는 stack
            stack.append(a)
        else: # 연산자 ㅡ 두번쨰 연산자부터는 비교
            while stack and order.get(stack[-1],0) >= order.get(a, 0):
                result.append(stack.pop())
            stack.append(a)

    while stack:
        result.append(stack.pop())

    return result

# 후위표기법 계산
def evaluate_postfix(arr):

    stack = []

    for a in arr:

        if a.isdigit(): # 피연산자 ㅡ 무조건 stack
            stack.append(int(a))
        else: # 연산자 ㅡ 피연산자2개 꺼내서 연산후, 결과값은 stack에 추가
            n2 = stack.pop()
            n1 = stack.pop()

            if a == '+':
                stack.append(n1+n2)
            elif a == '-':
                stack.append(n1-n2)
            elif a == '*':
                stack.append(n1*n2)
            elif a == '/':
                stack.append(n1/n2)

    return stack.pop()

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(input().strip())

    data2 = infix_to_postfix(data)
    data3 = evaluate_postfix(data2)

    print(f'#{test_case}', data3)