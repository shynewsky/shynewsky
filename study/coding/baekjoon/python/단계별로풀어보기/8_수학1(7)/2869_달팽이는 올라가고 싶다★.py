# 방1)
# 시간초과

import sys
sys.stdin = open('input.txt')

# 입력
A, B, V = map(int, input().split())
# 변수
count = 0
height = 0

while height < V:

    count += 1
    if count%2 == 1:
        height += A
    elif count%2 == 0:
        height -= B

print((count+1)//2)

# 방2)
# 피자나누기

# 입력
A, B, V = map(int, input().split())
move = A-B
goal = V-1
print(goal + (move-1) // move + 1)

'''
경우의 수
1) A로 끝나거나 ㅡ 항상
2) B로 끝나거나 ㅡ 미끄러지지 않기 때문에 불가능

경우의 수
1) A로 종점을 지나치는 경우
2) A와 종점이 일치하는 경우
3) A로 종점이 닿지 않는 경우 ㅡ (1)로 끝나야한다

경우의 수
1) [A-B]씩 이동하다가, 마지막 A가 종점을 지나치는 경우
2) [A-B]씩 이동하다가, 마지막 A가 종점과 일치하는 경우
=> 이동단위 [A-B]
=> 남은길이가 A이하여야 한다
=> [A-B]단위로 [V-A]이상을 가야하고, 기본 1일을 채우고 간다
'''
