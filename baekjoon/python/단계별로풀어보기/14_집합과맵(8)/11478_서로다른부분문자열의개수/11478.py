import sys
sys.stdin = open('input.txt')

S = input()
li = []
cnt = 0
for start_idx in range(0, len(S)):
    for end_idx in range(start_idx+1, len(S)+1):
        string = S[start_idx:end_idx]
        if string not in li:
            li.append(string)
            cnt += 1

print(cnt)