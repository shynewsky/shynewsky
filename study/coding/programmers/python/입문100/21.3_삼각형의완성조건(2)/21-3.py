# 삼각형의 세 변이 a < b < c 일때, c < a+b 이어야 한다
# [a, b] (0<a<b) 일때, 나머지 한 변 x의 길이 범위는?
# - b가 가장 클때, b < a+x 이므로, b-a < x <= b
# - x가 가장 클때, x < a+b 이므로, b <= x < a+b
# 따라서 b-a < x < a+b 에 해당되는 정수 개수를 구한다

def solution(sides):
    a = min(sides)
    b = max(sides)
    x = [i for i in range(b-a+1, a+b)]
    return len(x)

print(solution([1,2]))
