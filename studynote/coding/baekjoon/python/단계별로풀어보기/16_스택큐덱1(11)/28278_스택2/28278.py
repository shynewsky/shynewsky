import sys
sys.stdin = open('input.txt')

N = int(input())
s = []
for n in range(N):
    cmd = input()

    if cmd[0] == '1':
        s.append(cmd[2:])
    elif cmd[0] == '2':
        if s: print(s.pop())
        else: print(-1)
    elif cmd[0] == '3':
        print(len(s))
    elif cmd[0] == '4':
        if s: print(0)
        else: print(1)
    elif cmd[0] == '5':
        if s: print(s[0])
        else: print(-1)
