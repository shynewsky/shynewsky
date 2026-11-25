def solution(n, arr1, arr2):
    out = []
    for i in range(n):
        v = arr1[i] | arr2[i]
        row = ''.join('#' if (v >> (n - 1 - j)) & 1 else ' ' for j in range(n))
        out.append(row)
    return out

# -----------------------------------------------------------------------------------------

def solution(n, arr1, arr2):
    trans = str.maketrans({'1': '#', '0': ' '})
    fmt = f'0{n}b'
    return [format(arr1[i] | arr2[i], fmt).translate(trans) for i in range(n)]
