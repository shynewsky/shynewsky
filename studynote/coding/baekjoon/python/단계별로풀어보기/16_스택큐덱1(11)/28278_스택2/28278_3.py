import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
s = []
out = []

for _ in range(N):
    cmd = input().rstrip()
    c = cmd[0]

    if c == '1':
        s.append(cmd[2:])
    elif c == '2':
        out.append(s.pop() if s else -1)
    elif c == '3':
        out.append(len(s))
    elif c == '4':
        out.append(0 if s else 1)
    else:
        out.append(s[-1] if s else -1)

sys.stdout.write("\n".join(map(str, out)))
