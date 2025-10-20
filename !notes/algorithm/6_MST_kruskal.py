import sys
sys.stdin = open('input.txt')

# 입력 ----------------------------------------------------------------------------

V, E = map(int, input().split())

adj_list = []
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_list.append((n1, n2, w))

adj_list.sort(key=lambda x : x[2]) # [2]번을 기준으로 오름차순 정렬

# 함수 ----------------------------------------------------------------------------

parents = [i for i in range(V+1)] # make_set()

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return
    parents[ry] = rx

# 코드 ----------------------------------------------------------------------------

cnt = 0        # 현재까지 선택한 간선의 수
min_weight = 0 # 가중치의 합

for n1, n2, w in adj_list:

    if find_set(n1) != find_set(n2): # 사이클이 아니라면(같은 집합이 아니라면)
        union(n1, n2)                # 사이클 생성(같은 집합으로 연결하기)
        cnt += 1
        min_weight += w

        if cnt == V-1:               # 간선 (V-1)개 선택해서 = MST 완성되면 종료
            break
    