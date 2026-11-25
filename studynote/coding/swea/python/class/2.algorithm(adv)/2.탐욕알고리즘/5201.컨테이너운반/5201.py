def move(containers, trucks):
    total = 0
    for i in range(M): # 적재용량이 가장 큰 트럭부터 순회
        for j in range(N): # 무게가 가장 큰 컨테이너부터 순회
            if containers[j] == -1 : # 운반불가일 경우
                continue             # 다음 컨테이너 확인
            if containers[j] <= trucks[i]: # 트럭에 실을 수 있는 컨테이너의 경우
                total += containers[j]  # 총 운반 용량에 누적하고
                containers[j] = -1      # 운반표시를 한다
                break
    return total

T = int(input())
for t in range(1, T+1):
    # 입력
    N, M = map(int, input().split()) # N 컨테이너 수, M 트럭 수 (1<=N,M<=100)
    W = sorted(list(map(int, input().split())), reverse=True) # N개 화물 무게 (1<=Wi, Ti<=50)
    T = sorted(list(map(int, input().split())), reverse=True) # M개 적재 용량
    # 풀이
    answer = move(W, T)
    # 출력
    print(f'#{t}', answer)


