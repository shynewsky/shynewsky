# 1. LCA 찾는 함수 ---------------------------------
def find_lca(a, b):
    visited = [0] * (V+1)
    while a:
        visited[a] = 1
        a = par[a]
    while b:
        if visited[b] == 1:
            return b
        b = par[b]
    return 1 # 최종 LCA는 루트노드

# 2. 서브트리 크기 찾는 함수 --------------------------
def dfs_subtree(root):
    s = [root]
    cnt = 0
    while s:
        x = s.pop()
        cnt += 1
        if left[x]:
            s.append(left[x])
        if right[x]:
            s.append(right[x])

    return cnt

# 입력 ----------------------------------------------
T = int(input())
for t in range(1, T+1):
    V, E, A, B = map(int, input().split())
    data = list(map(int,input().split()))

# 풀이 ----------------------------------------------
# 1. 가장 가까운 공통조상(LCA)를 찾고
    # par[] 활용
    # A부터 루트까지 올라가며 조상들을 표시
    # B부터 루트까지 올라가며, 공통 조상을 찾으면 LCA
# 2. LCA를 루트로 하는 서브트리의 정점 개수 구하기
    # left[], right[] 활용
    # LCA에서 시작해서 자식방향으로 DFS/BFS
    # 방문한 노드수 카운트

# 전처리 --------------------------------------------
    par = [0] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = data[i*2], data[i*2+1]
        par[c] = p
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # print(par)
    # print(left)
    # print(right)

# 코드 ----------------------------------------------

    lca = find_lca(A, B)
    size = dfs_subtree(lca)

    # print(lca)
    # print(size)

# 출력 -----------------------------------------------

    print(f'#{t} {lca} {size}')

