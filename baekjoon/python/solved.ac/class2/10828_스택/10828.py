import time
start = time.time()
# -----------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push': s.append(cmd[1])
    elif cmd[0] == 'pop':
        try : print(s.pop())
        except : print(-1)
    elif cmd[0] == 'size': print(len(s))
    elif cmd[0] == 'empty':
        if s: print(0)
        else: print(1)
    elif cmd[0] == 'top':
        try : print(s[-1])
        except : print(-1)
# -----------------
end = time.time()
print(end-start, '초')