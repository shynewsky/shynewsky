import sys
sys.stdin = open('input.txt')

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

        if a.isdigit() : # 피연산자 ㅡ 무조건 result에 들어간다
            result.append(a)
        elif a == '(': # 열린괄호 ㅡ 무조건 stack에 들어간다
            stack.append(a)
        elif a == ')': # 닫힌괄호 ㅡ stack에서 열린괄호가 나올때까지, stack에 있던 연산자를 result로 이동
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop() # 열린괄호 만나면 stack에서 소거
        else: # 연산자 ㅡ stack에 우선순위가 같거나 높은게 있으면, 상대를 result로 이동시키고, 본인은 stack에 들어감
            while (stack and stack[-1] != '('
                and order.get(stack[-1], 0) >= order.get(a, 0)): # 키가 없을때 None 반환되는것 방지용
                result.append(stack.pop())
            stack.append(a)

    while stack: # stack에 남은 연산자도 모두 result 로 이동
        result.append(stack.pop())

    return result

# 후위표기법 계산
def evaluate_postfix(arr):

    stack = [] # 피연산자

    for a in arr:

        if a.isdigit(): # 피연산자는 무조건 stack으로
            stack.append(int(a))

        else: # 연산자면 ㅡ stack에서 피연산자 두개를 꺼내 연산을 수행하고, 다시 stack에 넣는다
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

T = int(input())
for test_case in range(1, T+1):

    data = list(input())
    data2 = infix_to_postfix(data)
    data3 = evaluate_postfix(data2)

    print(data3)

