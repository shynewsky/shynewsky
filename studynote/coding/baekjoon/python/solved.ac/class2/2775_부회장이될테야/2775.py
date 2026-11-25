import sys
sys.stdin = open('input.txt')
from pprint import pprint

apartment = [[0] * 15 for _ in range(15)]
# 0층
for i in range(15):
    apartment[0][i] = i
# 1~14층
for i in range(1, 15): # 층
    apartment[i] = apartment[i-1][:]
    for j in range(1, 15): # 호
        apartment[i][j] += apartment[i][j-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n])