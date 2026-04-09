# DFS(재귀)
'''
방문표시 후
출력하기

for문으로 돌며 다음 노드 탐색
    간선이 있고, 방문하지 않은 노드라면
        다음노드 탐색
'''

#--------------------------------------------------

visited = [0] * (V+1)
result = []

#--------------------------------------------------

# 인접행렬

def DFS4(current_node): # 인접행렬
    visited[current_node] = 1
    result.append(current_node)

    for next_node in range(1, V+1): # 오름차순 정렬
        if adj_mat[current_node][next_node] == 1 and visited[next_node] == 0:
            DFS4(next_node)

#--------------------------------------------------

# 인접리스트

def DFS5(current_node): # 인접리스트
    visited[current_node] = 1
    result.append(current_node)

    for next_node in sorted(adj_list[current_node]): # 오름차순 정렬
        if visited[next_node] == 0:
            DFS5(next_node)

#--------------------------------------------------

# 인접딕셔너리

def DFS6(current_node): # 인접딕셔너리
    visited[current_node] = 1
    result.append(current_node)

    for next_node in sorted(adj_dict[current_node]): # 오름차순 정렬
        if visited[next_node] == 0:
            DFS6(next_node)
