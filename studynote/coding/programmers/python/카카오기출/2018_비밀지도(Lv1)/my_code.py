def solution(n, arr1, arr2):
    # 10진수를 n자릿수의 2진수로 바꾸는 방법 ==> format(num, f'0{n}b')
    # 근데 2진수끼리 '|' 연산을 하려면 10진수로 바꿔야 한다
    # 자릿수를 맞추지 않아도 10진수끼리 먼저 계산해도 결과는 같으므로, 2진수로 변환하기 전에 먼저 계산한다

    arr3 = []
    for i in range(n):
        arr3.append(format(arr1[i] | arr2[i], f'0{n}b'))

    arr4 = []
    for a in arr3:
        temp = ''
        for b in a:
            temp += '#' if b == '1' else ' '
        arr4.append(temp)

    return arr4
