"""
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
"""

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split()) # V 노드개수, E 간선개수
data = list(map(int, input().split())) # E쌍 관계도

# 인접 행렬 생성
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# BFS 함수 생성
def BFS_queue(start):

    visited = [0] * (V+1) # 방문 여부 리스트
    q = []                # 큐 초기화

    visited[start] = 1    # 시작노드 방문 처리 후
    q.append(start)       # 큐에 삽입

    while q : # 큐에 원소가 있을때
        current_node = q.pop(0)      # 맨 앞에서 원소 제거

        print(current_node, end=' ')

        for next_node in range(1, V+1):
            if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                visited[next_node] = 1 # 다음노드도 방문처리 후
                q.append(next_node)    # 큐에 삽입

BFS_queue(1)

