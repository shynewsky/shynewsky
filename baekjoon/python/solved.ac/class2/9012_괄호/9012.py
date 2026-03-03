import time
start = time.time()
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = list(input().strip())
    s = []

    while string :
        letter = string.pop()

        if not s: # 비어있으면
            s.append(letter)
        elif letter == ')':
            s.append(letter)
        elif letter == '(':
            if s[-1] == '(':
                s.append(letter)
            elif s[-1] == ')':
                s.pop()
    if s:
        print('NO')
    else:
        print('YES')
# --------------------
end = time.time()
print(end-start, '초')