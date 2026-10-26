import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):

    N, arr = input().split()
    N = int(N)
    arr = list(map(int, arr.strip()))

    s = []

    for a in arr:

        if a not in s: # 스택에 없으면
            s.append(a)
        elif a in s:   # 스택에 있으면
            if s[-1] == a: # 마지막 원소가 같으면
                s.pop()
            else: # 스택에 있는데 마지막원소가 아니면
                s.append(a) # 그대로 그냥 추가

    print(f'#{test_case}', ''.join([str(n) for n in s]))

