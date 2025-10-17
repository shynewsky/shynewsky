import sys
sys.stdin = open('input.txt')

# 입력받기
N, M = map(int, input().split()) # 전체 N명, 최대 M명씩

"""
matrtix = [
    [1학년 여자 수, 1학년 남자 수]
    [2학년 여자 수, 2학년 남자 수]
    [3학년 여자 수, 3학년 남자 수]
    [4학년 여자 수, 4학년 남자 수]
    [5학년 여자 수, 5학년 남자 수]
    [6학년 여자 수, 6학년 남자 수]
]
"""

matrix = [[0] * 2 for _ in range(6)]

for _ in range(N) :
    gender, age = map(int, input().split())
    matrix[age-1][gender] += 1

count = 0 # 방 개수

for i in range(6) : # 학년 순회
    for j in range(2) : # 성별 순회

        # matrix[i][j] - 학년/성별 수
        # M 으로 나눠서, 몫이 0이 될때까지 M 으로 나누고, count+=1
        # 학생수가 0 이면 방을 배정하지 않는다
        if matrix[i][j] == 0 :
            #break - 다른 j 를 돌지 않고 바로 i 로 나가버린다
            continue # 다음 j를 돈다

        count += (matrix[i][j] + (M-1)) // M

print(count)

