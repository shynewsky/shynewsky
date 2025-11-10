def solution(nums):
    dict = {}
    for n in nums:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    select = len(nums) // 2
    length = len(dict)

    if select > length:
        return length
    else:
        return select