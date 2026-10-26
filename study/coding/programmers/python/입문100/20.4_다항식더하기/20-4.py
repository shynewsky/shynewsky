def solution(polynomial):
    li = polynomial.split(' + ')

    # '='은 없다
    # 연산자는 '+'만 있다
    # 변수는 'x'만 있다
    # ["3x","7","x"]
    for i in range(len(li)):
        if li[i] == 'x':
            li[i] = '1x'

    # 'x'만 있는 경우, '1'을 붙여준다
    # ["3x","7","1x"]
    x_num = 0 # 계수 합
    n_num = 0 # 정수 합
    for i in li:
        if 'x' in i : # 계수일 경우
            x_num += int(i[:-1])
        else : # 숫자일 경우
            n_num += int(i)

    # 계수가 0일때도 있고, 상수가 0일때도 있다
    # 계수가 1일때는 그냥 'x'로 작성해야 한다
    # 계수가 -1일때는 그냥 '-x'로 작성해야 한다
    if x_num == 0 and n_num == 0: return '0'
    elif x_num == 0 and n_num != 0: return f'{n_num}'
    elif x_num != 0 and n_num == 0:
        if x_num == 1: return f'x'
        elif x_num == -1: return f'-x'
        else : return f'{x_num}x'
    elif x_num != 0 and n_num != 0:
        if x_num == 1: return f'x + {n_num}'
        elif x_num == 1: return f'-x + {n_num}'
        else : return f'{x_num}x + {n_num}'

