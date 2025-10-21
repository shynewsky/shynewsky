import sys
sys.stdin = open("input.txt")

'''
- Union-find 사용
- 간선을 튜플로 갖는 일차원 리스트를 만들어 사용한다
'''

# 함수 -------------------------------------------------------

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
    parents[ry] = rx

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
    parents = [i for i in range(V)]

    for n1, n2, w in edges_list:
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            min_weight += w

            if cnt == V - 1:
                break

    print(f'#{t}', min_weight)




# import sys
# sys.stdin = open('input.txt')
#
# # 입력 ----------------------------------------------------------------------------
#
# V, E = map(int, input().split())
#
# adj_list = []
# for _ in range(E):
#     n1, n2, w = map(int, input().split())
#     adj_list.append((n1, n2, w))
#
# adj_list.sort(key=lambda x : x[2]) # [2]번을 기준으로 오름차순 정렬
#
# # 함수 ----------------------------------------------------------------------------
#
# parents = [i for i in range(V+1)] # make_set()
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
# # 코드 ----------------------------------------------------------------------------
#
# cnt = 0        # 현재까지 선택한 간선의 수
# min_weight = 0 # 가중치의 합
#
# for n1, n2, w in adj_list:
#
#     if find_set(n1) != find_set(n2): # 사이클이 아니라면(같은 집합이 아니라면)
#         union_set(n1, n2)                # 사이클 생성(같은 집합으로 연결하기)
#         cnt += 1
#         min_weight += w
#
#         if cnt == V-1:               # 간선 (V-1)개 선택해서 = MST 완성되면 종료
#             break
#
# print(min_weight)