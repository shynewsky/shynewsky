def solution(spell, dic):
    N = len(spell)
    ans = 2

    for word in dic :
        count = 0
        for char in spell:
            if char not in word:
                break
            count += 1
        if count == N:
            ans = 1
            break

    return ans
