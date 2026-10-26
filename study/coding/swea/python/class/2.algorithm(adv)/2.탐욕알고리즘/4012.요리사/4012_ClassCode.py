import sys
sys.stdin = open('input.txt')

def recur(n, start): # 조합 만드는 함수
    global min_val

    if n == N//2:
        syA, syB = division()
        if min_val > abs(syA-syB):
            min_val = abs(syA-syB)
        return

    # for i in range(N-1):
    #     for j in range(i+1, N):
    for i in range(start+1, N):
        if visited[i]:
            continue
        visited[i] = 1
        recur(n+1, i) # 중복조회를 줄이기 위해 start 매개변수 주기
        visited[i] = 0

def division(): # visited 에 따라 pathA, pathB 나누는 함수
    pathA, pathB = [], []
    for i in range(N):
        if visited[i]:
            pathA.append(i)
        else:
            pathB.append(i)
    return synergy(pathA), synergy(pathB)

def synergy(li): # 각 식재료 조합에 따른 맛 구하는 함수 - 조합
    val = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
           val += mat[li[i]][li[j]] + mat[li[j]][li[i]]
    return val

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # 변수
    min_val = 21e8
    visited = [0] * N
    # path = [] --> visited 된지 여부에 따라 A[] B[]로 나눌 것이기 떄문에 함수 내 지역변수로 사용
    # 코드
    recur(0, 0)
    # 출력
    print(f'#{t}', min_val)
