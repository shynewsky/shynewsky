import sys
sys.stdin = open('input.txt')

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

# 입력 -------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    # 간선리스트
    edges_list = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges_list.append((n1, n2, w))
    edges_list.sort(key=lambda x: x[2])

    # 코드 -----------------------------------------------------

    cnt = 0     # 현재까지 선택한 간선의 수
    min_weight = 0  # 가중치의 합

    # make_set
    parents = [i for i in range(V+1)]

    for n1, n2, w in edges_list:
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            min_weight += w

            if cnt == V - 1:
                break

    print(f'#{t}', min_weight)


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    edges.sort(key=lambda x: x[2])  # 가중치를 기준으로 오름차순으로 정렬

    cnt = 0     # 선택한 간선의 수
    result = 0  # 가중치의 합

    parents = [i for i in range(V + 1)]

    for u, v, w in edges:

        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += w

            if cnt == V:
                break

    print(f'#{tc} {result}')


# # 함수 -----------------------------------------------------------
#
# def find_set(x):
#     if x == parents[x]:
#         return x
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
# def union_set(x, y):
#     rx = find_set(x)
#     ry = find_set(y)
#     if rx == ry:
#         return
#     parents[ry] = rx
#
# # 입력 -----------------------------------------------------------
# T = int(input()) # 테스트케이스
# for t in range(1, T+1):
#     V, E = map(int, input().split()) # V 마지막노드번호, E 간선개수
#
#     adj_list = []
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         adj_list.append((n1, n2, w))
#
#     adj_list.sort(key=lambda x : x[2]) # 가중치 기준으로 오름차순
#
#     # 코드 -----------------------------------------------------------
#
#     parents = [i for i in range(V+1)] # make_set()
#
#     cnt = 0 # 선택한 간선 수
#     min_weight = 0 # 가중치의 합
#
#     for n1, n2, w in adj_list:
#         if find_set(n1) != find_set(n2):
#             union_set(n1, n2)
#             cnt += 1
#             min_weight += w
#
#             if cnt == V-1:
#                 break
#
#     print(f'#{t}', min_weight)