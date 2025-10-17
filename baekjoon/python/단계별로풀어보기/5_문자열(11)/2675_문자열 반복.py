T = int(input())
for test_case in range(T):
    R, S = input().split()
    for char in S:
        print(char * int(R), end='')
    print()
