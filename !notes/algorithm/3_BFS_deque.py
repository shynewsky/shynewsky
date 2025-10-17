# BFS(큐,데크)
from collections import deque
'''
start는 입력받는다
q 리스트를 start로 초기화한다
visited를 패딩하여 만든다

"큐가 빌때가지 반복하여 돈다"
    현재 원소를 지정한다
    출력한다

    현재 행을 돌면서 당므 원소를 지정한다 (오름차순 유지)
        만약 간선이 있고, 방문한 적이 없으면
            방문표시 후
            다음 방문 지점으로 추가한다
'''
'''
DFS는 꺼내면서 방문처리를 하는데, BFS는 방문처리하고 추가한다
'''

#--------------------------------------------------

# 인접행렬

def BFS1(start):
    q = deque()
    visited = [0] * (V+1)
    result = []

    visited[start] = 1
    q.append(start)

    while q:
        currrent_node = q.popleft()
        result.append(currrent_node)

        for next_node in range(1, V+1):
            if adj_mat[currrent_node][next_node] == 1 and visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)

    return result

#--------------------------------------------------








# 인접리스트

def BFS2(start):
    for i in range(1, V+1):
        adj_list[i].sort()

    q = deque()
    visited = [0] * (V+1)
    result = []

    visited[start] = 1
    q.append(start)

    while q:
        current_node = q.popleft()
        result.append(current_node)

        for next_node in adj_list[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)

    return result

#--------------------------------------------------

# 인접딕셔너리

def BFS3(start):
    q = deque()
    visited = [0] * (V+1)
    result = []

    visited[start] = 1
    q.append(start)

    while q:
        current_node = q.popleft()
        result.append(current_node)

        for next_node in adj_dict[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)

    return result
