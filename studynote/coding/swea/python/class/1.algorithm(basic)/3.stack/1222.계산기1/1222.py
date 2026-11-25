#  후위표기법 변화
def infix_to_postfix(arr):

    stack = [] # 연산자
    result = [] # 피연산자, 연산자

    for a in arr:
        if a.isdigit(): # 피연산자 ㅡ result에 추가
            result.append(a)
        else: #연산자 ㅡ stack에 추가 (연산자가 1개여서 우선순위 평가 필요 없음)
            stack.append(a)

    while stack: # 피연산자 다 쌓으면, 연산자 쏟아넣기
        result.append(stack.pop())

    return result

# 후위표기법 계산
def evaluate_postfix(arr):

    stack = []

    for a in arr:

        if a.isdigit(): # 피연산자 ㅡ stack에 추가
            stack.append(int(a))
        else: # 연산자 ㅡ 피연산자 2개 꺼내서 연산후, stack에 추가
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1+n2)

    return stack.pop()

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(input().strip())

    data2 = infix_to_postfix(data)
    data3 = evaluate_postfix(data2)

    print(f'#{test_case}', data3)

