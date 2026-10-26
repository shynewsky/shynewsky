import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 단어개수
words_set = set(input().strip() for _ in range(N))
words_list = []
for word in words_set:
    length = len(word)
    words_list.append([length, word])
words_list.sort()
print('\n'.join(l for w, l in words_list))
# ------------------
end = time.time()
print(end-start, '초')