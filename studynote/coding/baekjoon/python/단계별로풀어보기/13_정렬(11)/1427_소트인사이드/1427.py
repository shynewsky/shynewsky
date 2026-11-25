import sys
sys.stdin = open('input.txt')

N = sorted(list(map(int, input().strip())), reverse=True)
print(''.join(map(str,N)))
