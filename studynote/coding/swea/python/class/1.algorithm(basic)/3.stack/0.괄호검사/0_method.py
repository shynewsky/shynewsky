# 메서드 활용

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    arr = list(input()) # 공백도 들어간다

    s = [] # 열린괄호만 넣을 것. 닫힌괄호가 나오면 열린괄호 소거
    ok = True

    for a in arr:

        if a in '(': # 열린괄호면 ㅡ 바로 넣기
            s.append(a)

        elif a in ')': # 닫힌괄호면
            if len(s) == 0 : # 비어있으면 탈출
                ok = False
                break
            elif s[-1] == '(' : # 열린괄호 있으면, 소거
                s.pop()

    if len(s) != 0 : # 열린괄호가 모두 소거되지 않았으면
        ok = False

    print(ok)
