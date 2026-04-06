# ChatGPT

import heapq

def solution(program):

    # 호출 시각 기준 정렬
    program.sort(key=lambda x: x[1])

    answer = [0] * 11

    time = 0
    i = 0
    n = len(program)

    heap = []

    while i < n or heap:

        # 실행할 게 없으면 시간 점프
        if not heap and time < program[i][1]:
            time = program[i][1]

        # 현재 시간까지 호출된 프로그램 heap에 추가
        while i < n and program[i][1] <= time:
            score, call, duration = program[i]
            heapq.heappush(heap, (score, call, duration))
            i += 1

        # 실행
        score, call, duration = heapq.heappop(heap)

        wait_time = time - call
        answer[score] += wait_time

        time += duration

    answer[0] = time

    return answer