import sys
sys.stdin = open('input.txt')

# 함수 --------------------------------------------------------------

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry: # 같은 집합이면 합치지 않음
        return
    parents[ry] = rx

# 입력 --------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    edges = [] # 간선리스트
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))
    edges.sort(key=lambda x: x[2]) # 가중치 기준으로 오름차순

    # 코드 --------------------------------------------------------------

    parents = [i for i in range(V + 1)]  # make_set()

    cnt = 0 # 선택한 간선의 수
    min_weight = 0 # 가중치의 합

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2): # 같은 집합이 아니면 연결한다
            union_set(n1, n2)
            cnt += 1
            min_weight += w

            if cnt == V:
                break

    # 출력 --------------------------------------------------------------

    print(f'#{t}', min_weight)
