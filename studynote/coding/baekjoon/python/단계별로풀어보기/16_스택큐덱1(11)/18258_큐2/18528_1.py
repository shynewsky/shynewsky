import sys
sys.stdin = open('input.txt')
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
out = []

for _ in range(N):
    cmd = input().split()
    op = cmd[0]

    if op == 'push':
        q.append(cmd[1])
    elif op == 'pop':
        out.append(q.popleft() if q else -1)
    elif op == 'size':
        out.append(len(q))
    elif op == 'empty':
        out.append(0 if q else 1)
    elif op == 'front':
        out.append(q[0] if q else -1)
    elif op == 'back':
        out.append(q[-1] if q else -1)

sys.stdout.write("\n".join(map(str, out)))