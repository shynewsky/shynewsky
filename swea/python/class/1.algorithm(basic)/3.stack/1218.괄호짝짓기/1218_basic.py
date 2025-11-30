import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):

    N = int(input())
    arr = list(input())

    s = []
    ok = True

    for a in arr:

        if a in '({[<': # 열린괄호면 ㅡ 추가
            s.append(a)
        elif a in ')}]>': # 닫힌괄호면
            if len(s) == 0: # 열린괄호가 없으면, 싪패
                ok = False
                break
            elif a == ')' and s[-1] == '(':
                s.pop()
            elif a == '}' and s[-1] == '{':
                s.pop()
            elif a == ']' and s[-1] == '[':
                s.pop()
            elif a == '>' and s[-1] == '<':
                s.pop()
            else: # 쌍이 맞지 않으면
                ok = False
                break

    if len(s) != 0: # 열린괄호가 모두 소거되지 않았다면
        ok = False

    print(f'#{test_case}', int(ok))
