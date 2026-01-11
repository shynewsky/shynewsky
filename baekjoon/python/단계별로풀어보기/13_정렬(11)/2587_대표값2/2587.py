import sys
sys.stdin = open('input.txt')

li = [int(input()) for _ in range(5)]
avg = int(sum(li)/5)
med = sorted(li)[2]

print(avg)
print(med)