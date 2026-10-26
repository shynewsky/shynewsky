import sys
sys.stdin = open('input.txt')

S = input()
s = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        s.add(S[i:j+1])

print(len(s))