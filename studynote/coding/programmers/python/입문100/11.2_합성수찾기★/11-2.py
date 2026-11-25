def solution(n):
    total_count = 0
    for i in range(1, n+1):  # n 이하의 합성수 개수
        count = 0
        for j in range(1, i+1):  # i 가 가질 수 있는 약수는 i 보다 작은 수
            if i % j == 0:  # 나누어 떨어지면
                count += 1  # 약수 개수 증가
        if count > 2:  # 1과 자기 자신을 제외하고, 약수가 더 있으면
            total_count += 1
    return total_count
