import sys
from collections import deque

input = sys.stdin.readline

# --------------------- 1) 입력 ---------------------
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# --------------------- 2) 섬 라벨링 (BFS) ---------------------
# 0: 바다, 1: 땅  ->  섬을 1,2,3,... 로 새 라벨 부여
lab = [[0]*M for _ in range(N)]
dirs4 = [(-1,0),(1,0),(0,-1),(0,1)]

island_id = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 1 and lab[i][j] == 0:
            island_id += 1
            q = deque([(i,j)])
            lab[i][j] = island_id
            while q:
                x,y = q.popleft()
                for dx,dy in dirs4:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<M and A[nx][ny]==1 and lab[nx][ny]==0:
                        lab[nx][ny] = island_id
                        q.append((nx,ny))

K = island_id  # 섬 개수
if K <= 1:       # 섬이 0개/1개이면 다리 길이 합은 0
    print(0)
    sys.exit(0)

# --------------------- 3) 행/열 스캔으로 간선(다리) 생성 ---------------------
# 핵심: 각 행/열을 선형으로 보며 '섬-바다...바다-섬' 패턴만 간선 후보
# 길이가 2 이상인 경우만 허용. 같은 두 섬 사이의 간선은 최솟값만 보관.
edge_min = dict()  # key=(a,b) where a<b, val=min_distance

def add_edge(a, b, w):
    if a == b or w < 2:
        return
    if a > b:
        a, b = b, a
    prev = edge_min.get((a,b))
    if prev is None or w < prev:
        edge_min[(a,b)] = w

# 행 스캔
for i in range(N):
    last_island = 0  # 직전에 본 섬 라벨 (0은 바다/없음)
    zero_cnt = 0
    for j in range(M):
        cur = lab[i][j]
        if cur == 0:
            if last_island != 0:
                zero_cnt += 1
        else:  # 섬
            if last_island != 0:
                # 섬 ... (바다 zero_cnt) ... 섬
                add_edge(last_island, cur, zero_cnt)
            # 새 시작점으로 갱신
            last_island = cur
            zero_cnt = 0

# 열 스캔
for j in range(M):
    last_island = 0
    zero_cnt = 0
    for i in range(N):
        cur = lab[i][j]
        if cur == 0:
            if last_island != 0:
                zero_cnt += 1
        else:
            if last_island != 0:
                add_edge(last_island, cur, zero_cnt)
            last_island = cur
            zero_cnt = 0

edges = [(w,a,b) for (a,b), w in edge_min.items()]
if not edges:
    print(-1)
    sys.exit(0)

# --------------------- 4) Kruskal (Union-Find) ---------------------
parent = list(range(K+1))
rank = [0]*(K+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

edges.sort()  # w 기준 오름차순
ans = 0
taken = 0
for w,a,b in edges:
    if union(a,b):
        ans += w
        taken += 1
        if taken == K-1:
            break

# 모든 섬이 하나로 연결됐는지 확인
root = find(1)
for v in range(2, K+1):
    if find(v) != root:
        print(-1)
        break
else:
    print(ans)
