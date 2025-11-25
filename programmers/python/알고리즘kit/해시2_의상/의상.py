def solution(clothes):

    # 가공
    dict = {}
    for name, type in clothes:
        if dict.get(type):
            dict[type].append(name)
        else:
            dict[type] = [name]

    # 코드
    # 모든 경우의 수에서 '어떤 옷도 입지 않고 있는' 1을 빼면 되지 않을까

    cum = 0
    n = len(dict)
    for key, value in dict.items():
        cum += n * len(value)

    return cum if n==1 else cum-1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	)