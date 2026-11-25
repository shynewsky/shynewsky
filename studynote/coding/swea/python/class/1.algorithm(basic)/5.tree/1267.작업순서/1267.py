import heapq

# 1. 위상정렬 -----------------------------------------
def Topological_Sort():
    # 우선순위큐
    # - 번호가 작은 순서로 꺼내, 정렬된 결과를 얻을 수 있다 (일관적인 결과)
    # - "가능한 위상정렬이 여러개면 노드 번호가 작은것부터 출력하라" 조건이 있는 경우가 있다

    hq = []
    for n1 in range(1, V+1):
        if indegree[n1] == 0:
            heapq.heappush(hq, n1)

    result = []
    while hq:
        current_node = heapq.heappop(hq)
        result.append(current_node)
        for n2 in adj_list[current_node]: # 자식들
            indegree[n2] -= 1             # 선행작업 개수 감소
            if indegree[n2] == 0:         # 선행작업 조건 해제됐으면
                heapq.heappush(hq, n2)

    return result

# 입력 ------------------------------------------------
T = 10
for t in range(1, T+1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))

# 설계 ------------------------------------------------
    "위상정렬(Topological Sort)"
    # - 선행조건이 없는 작업부터 처리하고
    # - 해당 작업을 선행조건으로 갖고 있던 다음 작업들의 선행 조건을 하나씩 해제
    # 1. 진입차수 계산 : 선행작업 개수 계산 = 해당 노드로 들어오는 간선의 개수
    # 2. 시작점 찾기 : 진입차수가 0인 작업들을 큐에 넣는다
    # 3. 작업이 완료되면 진입차수를 1씩 감소시키고, 진입차수가 0이 된 작업은 큐에 추가

    "칸 알고리즘(Kahn's Algorithm)"
    # - 위상정렬을 구현하는 대표적인 방법

    "인접행렬,인접리스트,인접딕셔너리"
    # 인접행렬 : 간선 많을때, 가중치 존재 - 프림, 플로이드워셜, 워셜
    # 인접리스트 : 간선 적을때 - BFS/DFS, 위상정렬, 크루스칼 등
    # 인접딕셔너리 : 간선 적을때, 가중치 존재 - BFS/DFS, 다익스트라, 프림, 크루스칼 등
    '''
    graph = {i: {} for i in range(V+1)}
    for i in range(E):
        n1, n2, w = data[i*2], data[i*2+1], weights[i]
        graph[n1][n2] = w
        graph[n2][n1] = w  # 무방향이면 추가
    
    graph = {
        1: {2: 3, 3: 5},
        2: {1: 3, 4: 7},
        3: {1: 5, 5: 2, 6: 4},
        4: {2: 7, 7: 6},
        5: {3: 2, 8: 1, 9: 3},
        6: {3: 4, 10: 5, 11: 8},
        7: {4: 6, 12: 2},
        8: {5: 1},
        9: {5: 3},
        10: {6: 5},
        11: {6: 8, 13: 7},
        12: {7: 2},
        13: {11: 7}
    }
    '''

# 전처리 -----------------------------------------------
    # 위상정렬=인접리스트 사용
    adj_list = [[] for _ in range(V+1)]
    indegree = [0] * (V+1) # 진입차수
    for i in range(E):
        n1, n2 = data[i*2], data[i*2+1]
        adj_list[n1].append(n2) # 단방향
        indegree[n2] += 1 # 선행작업 개수 추가

    # print(adj_list)
    # print(indegree)

# 코드 --------------------------------------------------
    answer = Topological_Sort()

# 출력 --------------------------------------------------
    print(f'#{t}', *answer)
