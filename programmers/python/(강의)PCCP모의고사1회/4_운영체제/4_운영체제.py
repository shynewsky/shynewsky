# ChatGPT

import heapq

def solution(program):

    answer = [0] * 11                # 대기시간 합 반환용 리스트
    program.sort(key=lambda x: x[1]) # 호출 시각 기준 정렬

    pq = []             # 실행 대기중인 프로그램 저장
    time = 0            # 현재시각
    n = len(program)    # 전체 프로그램 개수
    i = 0               # 아직 pq에 넣지 않은 프로그램 인덱스

    # 아직 안 들어온 프로그램이 남아있거나, 실행중인 프로그램이 있을때
    while i < n or pq:

        # 실행할 게 없으면 시간 점프
        if not pq and time < program[i][1]:
            time = program[i][1]

        # 현재 시간까지 호출된 프로그램 pq에 추가
        while i < n and program[i][1] <= time:
            score, call, duration = program[i]
            # heapq.heappush(pq, program[i]) 가능하긴함
            heapq.heappush(pq, (score, call, duration))
            i += 1

        # 실행
        score, call, duration = heapq.heappop(pq)

        # 대기시간 기록
        wait_time = time - call
        answer[score] += wait_time

        # 현재시간 지남
        time += duration

    answer[0] = time

    return answer