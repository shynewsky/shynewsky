T = int(input())
matrix = [input() for _ in range(T)]

for string in matrix:
    print(string[0]+string[-1])
