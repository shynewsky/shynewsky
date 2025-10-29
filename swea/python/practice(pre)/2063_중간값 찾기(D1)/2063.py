N = int(input())

#a = list(input().split()) #이렇게 하면 문자열로 저장하게 됨
a = list(map(int, input().split())) #이렇게 하면 정수형으로 저장하게 됨

a.sort() #버블소팅 안해도 오름차순으로 정렬해줌
mid = N // 2 #N이 항상 홀수이기 때문에 2로 나눈 몫은 항상 정가운데 숫자

print(a[mid])