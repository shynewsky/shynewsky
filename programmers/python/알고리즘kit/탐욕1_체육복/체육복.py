def solution(n, lost, reserve):
    # 1로 채운 (n+1)개 배열 만들기
    arr = [1] * (n+1)

    # 잃어버린 사람은 0, 여벌을 가진 사람은 2로 채우기
    for i in lost:
        arr[i] = 0
    for i in reserve:
        arr[i] = 2

    # 내가 0일때 앞사람이 2이면 가져오기, 아니면 뒷사람이 2이면 가져오기
    for i in range(n):
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i-1] -= 1
                arr[i] += 1
            elif arr[i+1] == 2:
                arr[i+1] -= 1
                arr[i] += 1

    # 0 초과의 체육복을 갖고 있는 사람의 개수
    cnt = -1
    for a in arr:
        if a > 0:
            cnt += 1

    return cnt



solution(5, [2, 4], [1, 3, 5])