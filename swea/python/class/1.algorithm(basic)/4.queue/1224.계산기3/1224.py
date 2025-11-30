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
        elif a == '(': # 열린괄호 ㅡ 무조건 stack
            stack.append(a)
        elif a == ')': # 닫힌괄호 ㅡ stack에서 연산자는 result로 옮기고, 열린괄호는 소거
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else: # 연산자 ㅡ stack에 있는 것과 비교하여 우선순위 높은건 result에 넣는다
            while stack and stack[-1] != '(' and order.get(stack[-1],0) >= order.get(a,0):
                result.append(stack.pop())
            stack.append(a)

    while stack:
        result.append(stack.pop())

    return result

# 후위표기법 계산
def evaluate_postfix(arr):

    stack = []

    for a in arr:

        if a.isdigit(): # 피연산자
            stack.append(int(a))
        else: # 연산자
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

