# 오류 코드

def solution(n, numlist):
    for i in numlist:
        if i % n != 0:
            numlist.remove(i)  # 원소를 하나씩 빼면, 하나씩 앞으로 당겨지는데, 실시간 갱신 불가

    return numlist

# 역순으로 지워 나가면 된다

def solution(n, numlist):
    for i in numlist[::-1]:
        if i % n != 0:
            numlist.remove(i)

    return numlist

# 새 리스트를 만드는 방법도 있다

def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer
