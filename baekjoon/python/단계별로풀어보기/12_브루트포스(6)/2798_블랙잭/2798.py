import sys
sys.stdin = open('input.txt')

def recur(n, s):
    global max_sum

    if s > M:
        return

    if n == 3: # 종료조건 ㅡ 카드를 3개 뽑으면 종료
        if max_sum < s and s <= M:
            max_sum = s
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        # path.append(A[i])
        recur(n+1, s+A[i])
        # path.pop()
        visited[i] = 0
    pass

# 입력
N, M = map(int,input().split())
A = list(map(int, input().split()))
# 변수
path = []
visited = [0] * N
max_sum = 0
# 코드
recur(0, 0)
# 출력
print(max_sum)
