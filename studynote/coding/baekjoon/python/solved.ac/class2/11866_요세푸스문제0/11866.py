import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
start = [i for i in range(1, N+1)]
answer = []

i = K-1
while start:

    answer.append(start[i])
    start[i] = 0

    i += K
    while i >= N :
        i -= N
        cnt = start.count(0)
        for _ in range(cnt):
            start.remove(0)
        if not start:
            break
        N = len(start)

print(f"<{', '.join(map(str, answer))}>")