import sys
sys.stdin = open('input.txt')
from pprint import pprint

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_dict = {i:[] for i in range(V+1)} # 인접딕셔러니 생성
for i in range(E): # 인접딕셔너리 채워넣기
    n1, n2 = data[i*2], data[i*2+1]
    adj_dict[n1].append(n2)
    adj_dict[n2].append(n1)

print(adj_dict)

start = 1
s = [start]
visited = [0] * (V+1)

while s:
    current_node = s.pop() # 뒤에서 뽑아서

    if visited[current_node] == 0: # 방문하지 않았으면
        visited[current_node] = 1 # 방문 처리
        print(current_node, end='')

        for next_node in sorted(adj_dict[current_node], reverse=True): # 자식 노드 확인
            if visited[next_node] == 0: # 방문하지 않았으면, 스택에 넣기
                s.append(next_node)
