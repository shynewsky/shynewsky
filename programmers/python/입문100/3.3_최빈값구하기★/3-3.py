# 내 코드

def solution(array):
    array.sort()
    n = len(array)
    count = [1] * n
    cnt = 1
    for i in range(1, n):
        if array[i - 1] == array[i]:
            cnt += 1
            count[i] = cnt
        else:
            cnt = 1

    max_num = max(count)
    max_idx = count.index(max_num)
    max_cnt = 0
    for c in count:
        if c == max_num:
            max_cnt += 1
    if max_cnt == 1:
        return array[max_idx]
    return -1


# Counter 사용

from collections import Counter


def solution(array):
    count = Counter(array)  # 각 원소의 개수 세기
    max_freq = max(count.values())  # 최빈값의 등장 횟수
    mode = [k for k, v in count.items() if v == max_freq]  # 최빈값 후보들

    if len(mode) > 1:  # 최빈값이 여러 개라면
        return -1
    return mode[0]


# 딕셔너리 사용

def solution(array):
    freq = {}  # 빈도수를 저장할 딕셔너리

    # 각 숫자의 등장 횟수 세기
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # 가장 큰 빈도수 구하기
    max_freq = max(freq.values())

    # 최빈값 후보 찾기
    mode = [k for k, v in freq.items() if v == max_freq]

    # 최빈값이 여러 개면 -1 반환
    if len(mode) > 1:
        return -1
    return mode[0]
