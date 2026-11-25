# 내 코드

def solution(emergency):

    # 나보다 큰 수를 찾아라
    N = len(emergency)

    num_list = []
    for i in range(N): # 내 위치
        count = 0
        for j in range(N): # 비교대상
            if emergency[i] <= emergency[j]:
                count += 1
        num_list += [count]

    return num_list

# 딕셔너리 사용

def solution(emergency):
    sorted_em = sorted(emergency, reverse=True) # 내림차순으로 정렬
    rank = {v: i+1 for i, v in enumerate(sorted_em)} # 원소 → 순위 매핑
    return [rank[num] for num in emergency] # 원래 배열 순서대로 순위 출력
