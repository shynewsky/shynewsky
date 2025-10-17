# arr.sort(key=lambda x: x[1]) ㅡ 뒷쪽 원소 기준으로 나열하는 람다식
N = int(input())
x_list = [0] * N
y_list = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    x_list[i] = x
    y_list[i] = y
print((max(x_list)-min(x_list))*(max(y_list)-min(y_list)))
