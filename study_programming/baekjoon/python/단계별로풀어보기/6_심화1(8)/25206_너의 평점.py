import sys
sys.stdin = open('input.txt')

dict = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0,
}

# for line in sys.stdin:
#     subject, score, grade = line.split()

N = 20
matrix = [list(input().split()) for _ in range(N)]
total_sum = total_mul = 0
for subject, score, grade in matrix:
    if grade == 'P':
        N -= 1
        continue
    total_sum += float(score)
    total_mul += float(score) * dict[grade]
print(f'{total_mul/total_sum :.6f}')

