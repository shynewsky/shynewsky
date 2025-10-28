dict = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def solution(string):

    answer = ''

    N = len(string)
    i = 0

    while i < N:
        print(string[i])
        if string[i].isdigit():
            answer += string[i]
            i += 1
        else:
            start = i
            i += 1
            end = i

    return answer


    # while i < N:
    #     if string[i].isdigit():
    #         answer += string[i]
    #     i += 1
        # else: # 문자일때
        #     start = i
        #     while not string[i].isdigit():
        #         i += 1
        #     end = i
        #     answer += dict[string[start:end]]

result = solution('one4seveneight')
print(result)