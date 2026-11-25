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
        if string[i].isdigit():
            answer += string[i]
            i += 1
        # elif string[i:i + 3] in ['one', 'two', 'six']:
        elif string[i:i+3] in dict:
            answer += dict[string[i:i+3]]
            i += 3
        # elif string[i:i + 4] in ['zero', 'four', 'five', 'nine']:
        elif string[i:i+4] in dict:
            answer += dict[string[i:i+4]]
            i += 4
        # elif string[i:i+5] in ['three', 'seven', 'eight']:
        elif string[i:i+5] in dict:
            answer += dict[string[i:i+5]]
            i += 5
        # i += 1

    return int(answer)