def recur(n, arr):
    global max_val, visited

    val = ''.join(arr)

    # 가지치기 - 해당 단계에서 이미 만들어진 문자열일때
    if visited.get(n) and val in visited[n]:
        return

    # 방문표시 - 해당 단계가 처음이라면, 키와 값 자리를 만들어주고
    if n not in visited:
        visited[n] = set()
    visited[n].add(val) # 방문표시가 아니라, 문자열 자체를 넣는다

    # 중단조건 - max() 함수호출보다 if문 분기가 미세하게 더 빠르다
    if n == M: # int() 함수를 사용해도 if문 분기가 더 빠르다
        if max_val < int(val):
            max_val = int(val)
        return

    # 재귀호출 - 교환한 후에 재귀 진입, 나오면 다시 교환하여 원위치
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            recur(n+1, arr)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for t in range(1, T+1):
    # 입력
    arr, M = input().split()
    arr, N, M = list(arr), len(arr), int(M)     # 숫자열 자릿수, 교환 횟수
    # 변수
    max_val = 0
    visited = {} # 빈 딕셔너리
    # 코드
    recur(0, arr)
    # 출력
    print(f'#{t} {max_val}')

