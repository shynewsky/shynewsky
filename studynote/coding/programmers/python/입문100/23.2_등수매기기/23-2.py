def solution(score):
    score1 = [sum(i) for i in score]
    # 각 과목 평균이랑 비교하는 것이 아닌, 총 평균 비교
    # 평균이 높은 것은 총합이 높다는 것이기 때문에 총합만 구한다
    # [150,150,80,190,190,200,40]
    score2 = [0] * len(score)
    # score1 에서 최고값을 찾으면 순위를 넣을 리스트
    # score1 에서 최고값 순위를 기록하면, 점수를 -1로 바꿀 것이다
    rate = 1   # 동점자가 없을때 증가
    count = 1  # 사람수만큼 증가, 동점자가 없으면 순위에도 적용
    while max(score1) >= 0 : # 모든 숫자가 순위로 등록될때까지 진행
        max_num = max(score1)
        while True: # 같은 숫자를 모두 찾을때까지
            if max_num not in score1:
                break
            max_idx = score1.index(max_num)
            score2[max_idx] = rate
            score1[max_idx] = -1
            count += 1
        rate = count
    return score2
