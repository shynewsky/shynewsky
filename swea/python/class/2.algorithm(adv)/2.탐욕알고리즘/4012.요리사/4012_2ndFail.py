import sys
sys.stdin = open('input.txt')

def recur(n):

    if n == N//2:
        path2 = []
        for i in range(N):
            if i not in path:
                path2.append(i)
        total_path.add((tuple(path), tuple(path2)))
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        path.append(i)
        recur(n+1)
        path.pop()
        visited[i] = 0

def func(li):
    global max_synergy
    for s in li:
        A = s[0]
        B = s[1]
        syA = 0
        syB = 0
        for i in range(len(A)):
            for j in range(len(A)):
                syA += mat[A[i]][A[j]]
        for i in range(len(B)):
            for j in range(len(B)):
                syB += mat[B[i]][B[j]]
        if max_synergy < abs(syA-syB):
            max_synergy = abs(syA-syB)

T = int(input()) # 테스트케이스
for t in range(1, T+1):
    # 입력
    N = int(input()) # 행/열/식재료수
    mat = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    # 변수
    path = []
    visited = [0] * N
    total_path = set()
    max_synergy = 0
    # 재귀
    recur(0)
    total_path = sorted(list(total_path))
    print(total_path)
    # 시너지
    func(total_path)
    # 출력
    print(max_synergy)
