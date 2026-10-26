T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    V, E = map(int, input().split()) # V 노드개수, E 간선정보
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split()) # S 출발노드, G 도착노드

    # 인접행렬
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]
    for n1, n2 in data:
        adj_matrix[n1][n2] = 1
        adj_matrix[n2][n1] = 1

   # pprint(adj_matrix)

    # BFS
    q = []                  # 큐 만들기
    visited = [0] * (V+1)   # 방문리스트 만들기

    visited[S] = 1          # 시작노드 방문처리 후
    q.append(S)             # 큐에 삽입

    while q : # 큐에 원소가 있을때
        current_node = q.pop(0) # 맨 앞에서 원소 제거

        # ---------------------------------------
        if current_node == G :
            print(f'#{test_case}', visited[current_node]-1)
            break
        # ---------------------------------------

        for next_node in range(1, V+1): # 다음 노드 찾기
            if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                visited[next_node] = visited[current_node] + 1
                q.append(next_node)

    else:
        print(f'#{test_case}', 0)
