import sys

T = int(sys.stdin.readline()) # 5
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
