import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
out = []

N = int(input())
d = deque()
for n in range(N):
    cmd = list(input().split())
    c = cmd[0]

    if c == '1':
        d.appendleft(cmd[1])
    elif c == '2':
        d.append(cmd[1])
    elif c == '3':
        out.append(d.popleft() if d else -1)
    elif c == '4':
        out.append(d.pop() if d else -1)
    elif c == '5':
        out.append(len(d))
    elif c == '6':
        out.append(0 if d else 1)
    elif c == '7':
        out.append(d[0] if d else -1)
    elif c == '8':
        out.append(d[-1] if d else -1)

sys.stdout.write('\n'.join(map(str, out)))

