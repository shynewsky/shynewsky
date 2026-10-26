def solution(array, height):
    array.append(height) # 머쓱이까지 포함하고
    array.sort(reverse=True) # 키큰 사람부터 나열하고
    return array.index(height) # 머쓱이보다 키 큰 사람의 수를 반환한다
