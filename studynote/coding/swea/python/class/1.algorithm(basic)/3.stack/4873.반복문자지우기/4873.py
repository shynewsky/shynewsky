import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    arr = list(input().strip())

    s = []

    for a in arr:

        if a not in s: # 스택에 없으면 넣기
            s.append(a)
        elif a in s : # 스택에 있으면
            if s[-1] == a: # 마지막 원소이면
                s.pop()
            else: # 마지막원소는 아닌데, 스택에 있을때는
                s.append(a)

    print(f'#{test_case}', len(s))

