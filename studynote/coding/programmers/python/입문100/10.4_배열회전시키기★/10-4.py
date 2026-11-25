# 리스트 슬라이싱 활용

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]   # 마지막 요소를 맨 앞으로
    else:
        return numbers[1:] + [numbers[0]]     # 첫 번째 요소를 맨 뒤로
