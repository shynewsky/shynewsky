import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input()) # 이닝 수
data = [list(map(int, input().split())) for _ in range(N)] # 이닝별 선수 결과 데이터
'''
order = [? ? ? 0 ? ? ? ? ?]
ball = data[i][order[j]]     # 각 선수가 각 이닝에서 얻는 결과
'''
# ground = deque([0,0,0])      # 3루까지 비어있음
'''
1) result = 0 (아웃) 일때
   out += 1
   
2) result = 1 (안타/1루타) 일때
   ground.append(1)
   for _ in range(result)
        player = ground.popleft()
        if player: score += 1    

3) result = 2 (2루타) 일때
   ground.append(1)
   ground.append(0)
   for _ in range(result)
        player = ground.popleft()
        if player: score += 1    

4) result = 3 (3루타) 일때
   ground.append(1)
   ground.append(0)
   ground.append(0)
   for _ in range(result)
        player = ground.popleft()
        if player: score += 1    

4) result = 4 (홈런) 일때
   ground.append(1)
   ground.append(0)
   ground.append(0)
   ground.append(0)
   for _ in range(result)
        player = ground.popleft()
        if player: score += 1    
'''
# 테스트코드 -------------------------------------

ground = deque([1,1,1])

result = 1
score = 0
out = 0

if result:
    ground.append(1)
    for _ in range(result-1):
        ground.append(0)
    for _ in range(result):
        player = ground.popleft()
        if player: score += 1
else:
    out += 1

print(ground, score, out)

# ------------------------------------------------