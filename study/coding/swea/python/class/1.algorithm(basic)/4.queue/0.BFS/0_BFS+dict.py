import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_dict = {i : [] for i in range(V+1)} # 인접딕셔너리
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    adj_dict[n1].append(n2)
    adj_dict[n2].append(n1)

start = 1
q = [start]
visited = [0] * (V+1)

while q :
    current_node = q.pop(0)

    if visited[current_node] == 0: # 방문안했으면
        visited[current_node] = 1  # 방문 처리
        print(current_node, end=' ')

        for next_node in adj_dict[current_node]:
            if visited[next_node] == 0: # 방문안한 노드면
                q.append(next_node)     # 방문예정
