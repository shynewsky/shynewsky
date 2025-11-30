import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트케이스

for test_case in range(1, T+1):

    arr = list(input()) # 공백도 들어간다

    s = []
    ok = True

    for a in arr:

        if a in '({': # 열린괄호면 ㅡ 스택에 넣기
            s.append(a)
        elif a in ')}': # 닫힌괄호면
            if len(s) == 0: # 열린괄호가 없으면, 실패
                ok = False
                break
            elif a == ')' and s[-1] == '(':
                s.pop()
            elif a == '}' and s[-1] == '{':
                s.pop()
            else: # 짝이 맞지 않을때
                ok = False
                break

    if len(s) != 0 : # 열린괄호가 모두 소거되지 않았으면
        ok = False

    print(f'#{test_case}', int(ok))
