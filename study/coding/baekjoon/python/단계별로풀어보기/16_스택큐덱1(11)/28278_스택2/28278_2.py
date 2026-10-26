import sys
sys.stdin = open('input.txt')

N = int(input())
s = [''] * N
rear = 0 # rear 하나로 top, cnt 다 한다

for n in range(N):
    cmd = input()

    if cmd[0] == '1':
        s[rear] = cmd[2:]
        rear += 1
    elif cmd[0] == '2':
        if rear:
            rear -= 1
            print(s[rear])
        else: print(-1)
    elif cmd[0] == '3':
        print(rear)
    elif cmd[0] == '4':
        if rear: print(0)
        else: print(1)
    elif cmd[0] == '5':
        if rear: print(s[rear-1])
        else: print(-1)
