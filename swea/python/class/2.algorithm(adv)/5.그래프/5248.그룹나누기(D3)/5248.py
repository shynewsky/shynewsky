import sys
sys.stdin = open('input.txt')

# 2. find_set
def find_set(parents, x):
    # 방1) 반복문
    '''
    while parent_list[x] != x:
        x = parent_list[x]
    return x
    '''
    # 방2) 재귀
    if parents[x] != x:
        parents[x] = find_set(parents, parents[x])
    return parents[x]

# 3. union_set
def union_set(parents, ranks, x, y):
    rx = find_set(parents, x)
    ry = find_set(parents, y)
    if rx == ry: # 같은집합이면 합칠 필요 없음
        return

    # rank 큰것에 작은것 붙이기
    if ranks[ry] < ranks[rx]:
        parents[ry] = rx
    elif ranks[rx] < ranks[ry]:
        parents[rx] = ry
    else: # 높이가 같으면 ry 를 rx 밑에 두고 rank[rx] .높이 1증가
        parents[ry] = rx
        ranks[rx] += 1

# 입력 --------------------------------------------------------------------
T = int(input()) # 테스트케이스
for t in range(1, T+1):
    V, E = map(int, input().split()) # N(V) 노드개수, M(E) 간선개수
    data = list(map(int, input().split()))

    # 코드 -----------------------------------------------------------------

    # make_set
    parents = [i for i in range(V+1)]
    ranks = [0] * (V+1)

    # M번의 union() 수행
    for i in range(E):
        n1, n2 = data[i*2], data[i*2+1]
        union_set(parents, ranks, n1, n2)

    # 모든 노드에 대해 최종루트 갱신
    for i in range(1, V+1):
        parents[i] = find_set(parents, i)

    # 문제요구 : 0 제외, 1~N 중 set로 중복제거
    distinct_parents = set(parents) - {0}

    # 출력 ------------------------------------------------------------------
    print(f'#{t}', len(distinct_parents))
