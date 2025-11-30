q = [0] * 10
front = rear = -1 # 0이 아니라 -1로 초기화

rear += 1
q[rear] = 1

rear += 1
q[rear] = 2

rear += 1
q[rear] = 3

front += 1
print(q[front])

front += 1
print(q[front])

front += 1
print(q[front])
