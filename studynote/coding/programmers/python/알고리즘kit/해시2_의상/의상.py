def solution(clothes):

    # 가공
    dict = {}
    for name, type in clothes:
        if not dict.get(type):
            dict[type] = ['']
        dict[type].append(name)
    print(dict)

    # 코드
    # 모든 경우의 수에서 '어떤 옷도 입지 않고 있는' 1을 빼면 되지 않을까
    answer = 1
    for key, value in dict.items():
        answer *= len(value)
    print(answer)

    return answer - 1




solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	)