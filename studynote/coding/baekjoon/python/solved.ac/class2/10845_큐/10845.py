import time
start = time.time()
# ---------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push': q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif cmd[0] == 'size': print(len(q))
    elif cmd[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif cmd[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif cmd[0] == 'back':
        if q: print(q[-1])
        else: print(-1)
# ---------------------
end = time.time()
print(end-start,'초')