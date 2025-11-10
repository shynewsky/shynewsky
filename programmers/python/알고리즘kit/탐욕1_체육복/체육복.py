def solution(n, lost, reserve):
    # 1로 채운 (n+2)개 배열 만들기
    # 0번과 n+1번으로 패딩 넣기
    arr = [1] * (n+2)

    # 여벌을 가진 사람은 2로 채우기
    # 잃어버린 사람은 0으로 채우는 것이 아니라 -1 하기 (여벌 가져온 사람도 잃어버릴 수 있음)
    for i in reserve:
        arr[i] = 2
    for i in lost:
        arr[i] -= 1

    # 내가 0일때 앞사람이 2이면 가져오기, 아니면 뒷사람이 2이면 가져오기
    for i in range(1, n+1): # 범위주의
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i-1] -= 1
                arr[i] += 1
            elif arr[i+1] == 2:
                arr[i+1] -= 1
                arr[i] += 1

    # 0 초과의 체육복을 갖고 있는 사람의 개수
    cnt = -2
    for a in arr:
        if a > 0:
            cnt += 1

    print(cnt)
    return cnt

solution(3, [3], [1])