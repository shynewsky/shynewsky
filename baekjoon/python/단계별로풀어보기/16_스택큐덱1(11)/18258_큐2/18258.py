import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
q = deque()
for n in range(N):
    cmd = input()
    print(cmd)

    if cmd[:5] == 'push ':
        q.append(cmd[5:])
    elif cmd[:5] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif cmd[:5] == 'size':
        print(len(q))
    elif cmd[:5] == 'empty':
        if q: print(0)
        else: print(1)
    elif cmd[:5] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif cmd[:5] == 'back':
        if q: print(q[-1])
        else: print(-1)