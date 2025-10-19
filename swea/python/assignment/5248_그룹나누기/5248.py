import sys
sys.stdin = open('input.txt')

# 2. find_set
def find_set(parent_list, x):
    # 방1) 반복문
    '''
    while parent_list[x] != x:
        x = parent_list[x]
    return x
    '''
    # 방2) 재귀
    if parent_list[x] != x:
        parent_list[x] = find_set(parent_list, parent_list[x])
    return parent_list[x]

# 3. union_set
def union_set(parent_list, rank_list, a, b):
    root_a = find_set(parent_list, a)
    root_b = find_set(parent_list, b)
    if root_a != root_b:
        return



# 입력
T = int(input()) # 테스트케이스
for t in range(1, T+1):
    V, E = map(int, input().split()) # N(V) 노드개수, M(E) 간선개수
    data = list(map(int, input().split()))

    # make_set
    p = [i for i in range(V+1)]



