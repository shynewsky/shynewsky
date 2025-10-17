# 방1)

import sys
sys.stdin = open('input.txt')

string = input()
N = len(string)
i = 0
cnt = 0
while i < N:

    if string[i:i+2] == 'c=':
        cnt += 1
        i += 2
    elif string[i:i+2] == 'c-':
        cnt += 1
        i += 2
    elif string[i:i + 3] == 'dz=':
        cnt += 1
        i += 3
    elif string[i:i+2] == 'd-':
        cnt += 1
        i += 2
    elif string[i:i+2] == 'lj':
        cnt += 1
        i += 2
    elif string[i:i+2] == 'nj':
        cnt += 1
        i += 2
    elif string[i:i+2] == 's=':
        cnt += 1
        i += 2
    elif string[i:i+2] == 'z=':
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)

# 방2)

string = input()
N = len(string)
i = 0
cnt = 0
len2_str = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
len3_str = ['dz=']

while i < N:

    if string[i:i+2] in len2_str:
        cnt += 1
        i += 2
    elif string[i:i+3] in len3_str:
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)
