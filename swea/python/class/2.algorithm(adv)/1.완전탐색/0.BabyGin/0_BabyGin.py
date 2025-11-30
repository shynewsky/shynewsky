import sys
sys.stdin = open('input.txt')

# 조합
# 원소 6개 주어짐 'abcdef'-> 3개를 뽑는다

# 종료조건 : 3개를 모두 뽑았다면 종료
# - 시작점 : 0개를 고른 상태부터 시작
# 다음 재귀호출 구조 : 'abcdef' 중 하나를 고른다
# - 중복제거 : visited 한 숫자는 생략
# - 가지치기 : run 이나 triple 이 아니면 되돌아가기

def recur(n, idx):
    global isBabyGin

    if n == 3 :
        subset1 = path[::] # 깊은복사
        subset2 = [arr[i] for i in range(N) if visited[i] == 0]
        if babygin(subset1) and babygin(subset2):
            isBabyGin = True
        return

    for i in range(idx, N):
        if visited[i] == 1: # 왜 T/F 안써?
            continue

        visited[i] = 1
        path.append(arr[i])
        recur(n+1, i)

        path.pop()
        visited[i] = 0

def babygin(li):
    if li[0] == li[1] == li[2]: return True
    elif li[0]+1 == li[1] == li[2]-1: return True
    return False

T = int(input()) # 테스트케이스 수
for test_case in range(1, T+1):
    # 입력
    arr = sorted(list(map(int, input().strip())))
    N = len(arr)
    # 변수
    path = []               # 바구니
    visited = [False] * N   # 방문표시용
    isBabyGin = False
    # 재귀
    recur(0, 0)
    # 출력
    print(f'#{test_case}', isBabyGin)

