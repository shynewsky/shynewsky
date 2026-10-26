# 가위바위보 결과 판정 함수
def fight(x, y):  # x와 y는 학생 번호(인덱스)
    if cards[x] == cards[y]:   # 같은 패면 번호가 작은 쪽 승
        return x if x < y else y
    elif (cards[x] == 1 and cards[y] == 3) or \
         (cards[x] == 2 and cards[y] == 1) or \
         (cards[x] == 3 and cards[y] == 2):
        return x   # x가 이김
    else:
        return y   # y가 이김

# 토너먼트 (재귀 분할)
def backtracking(start, end):
    if start == end:   # 구간에 학생이 한 명만 있으면 그 사람이 승자
        return start

    mid = (start + end) // 2
    left = backtracking(start, mid)       # 왼쪽 그룹 승자
    right = backtracking(mid+1, end)      # 오른쪽 그룹 승자
    return fight(left, right)             # 둘 중 승자 반환

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    winner = backtracking(0, N-1)
    print(f'#{test_case} {winner+1}')  # 인덱스는 0부터라서 +1

