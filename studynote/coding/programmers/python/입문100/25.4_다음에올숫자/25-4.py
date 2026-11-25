def solution(common):
    l = r = 0
    if common[0] - common[1] == common[1] - common[2]:
        l = common[1] - common[0]
    else:
        r = common[1] / common[0]
    # 차가 같으면 등차
    # 차가 같지 않으면 등비

    if not r:  # 등차수열이면(간격이 0일수도 있기 때문)
        return common[-1] + l
    elif r:  # 등비수열이면
        return common[-1] * r

